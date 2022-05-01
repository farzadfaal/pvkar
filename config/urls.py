from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = i18n_patterns(
    path("", views.home, name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("profiles/", include("apps.profiles.urls", namespace="profiles")),
    # Your stuff: custom urls includes go here
    path("buildings/", include("apps.buildings.urls", namespace="buildings")),
    path("projects/", include("apps.projects.urls", namespace="projects")),
    path("services/", include("apps.services.urls", namespace="services")),
    path("proposals/", include("apps.proposals.urls", namespace="proposals")),
    path("plans/", include("apps.plans.urls", namespace="plans")),
    path("payments/", include("apps.payments.urls", namespace="payments")),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

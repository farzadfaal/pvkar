from django.urls import include, path

from apps.proposals.views import proposal_list_employer

from .views import (
    project_detail,
    project_detail_contractor,
    project_finalize,
    project_list,
    project_new,
    project_list_contractor,
    project_list_employer,
)

app_name = "projects"


urlpatterns = [
    path("", project_list, name="project_list"),
    path("employer", project_list_employer, name="project_list_employer"),
    path("contractor", project_list_contractor, name="project_list_contractor"),
    path(
        "contractor/<pk>/", project_detail_contractor, name="project_detail_contractor"
    ),
    path("new/", project_new, name="project_new"),
    path(
        "<project_id>/proposals/", include("apps.proposals.urls", namespace="proposals")
    ),
    path("<project_id>/", project_detail, name="project_detail"),
    path("<project_id>/finalize/", project_finalize, name="project_finalize"),
    path("<project_id>/services/", include("apps.services.urls", namespace="services")),
]

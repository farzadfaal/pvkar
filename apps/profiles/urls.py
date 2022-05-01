from django.urls import path

from .views import (
    certificate_detail,
    certificate_list,
    certificate_new,
    profile_detail,
    profile_update,
)

app_name = "profiles"


urlpatterns = [
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/update/", profile_update, name="profile_update"),
    path("certificates/", certificate_list, name="certificate_list"),
    path("certificates/new/", certificate_new, name="certificate_new"),
    path("certificates/<pk>/detail/", certificate_detail, name="certificate_detail"),
]

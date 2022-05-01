from django.urls import include, path

from .views import (
    building_detail,
    building_list,
    building_new,
    building_overview,
    building_publish,
    building_update,
)

app_name = "buildings"


urlpatterns = [
    path("", building_list, name="building_list"),
    path("new/", building_new, name="building_new"),
    path("<building_id>/", building_detail, name="building_detail"),
    path("<building_id>/overview/", building_overview, name="building_overview"),
    path("<building_id>/publish/", building_publish, name="building_publish"),
    path("<building_id>/update/", building_update, name="building_update"),
    path(
        "<building_id>/projects/", include("apps.projects.urls", namespace="projects")
    ),
]

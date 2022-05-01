from django.urls import path

from .views import (
    proposal_list_employer,
    proposal_new,
    proposal_detail_employer,
    proposal_list_contractor,
)

app_name = "proposals"


urlpatterns = [
    path("", proposal_list_contractor, name="proposal_list"),
    path(
        "<proposal_id>/employer/",
        proposal_detail_employer,
        name="proposal_detail_employer",
    ),
    path("employer", proposal_list_employer, name="proposal_list_employer"),
    path("<pk>/new/", proposal_new, name="proposal_new"),
]

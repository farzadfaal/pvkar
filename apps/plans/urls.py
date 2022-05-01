from django.urls import path

from .views import plan_buy_credit, plan_detail, plan_successful

app_name = "plans"


urlpatterns = [
    path("buy-credit/", plan_buy_credit, name="plan_buy_credit"),
    path("<pk>/detail/", plan_detail, name="plan_detail"),
]

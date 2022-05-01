from unicodedata import name

from django.urls import path

from .views import confirm_pay, create_pay, successful_pay

app_name = "payments"


urlpatterns = [
    path("<pk>/pay/", create_pay, name="create_pay"),
    path("<pk>/confirm/", confirm_pay, name="confirm_pay"),
    path("<pk>/successful/", successful_pay, name="successful_pay"),
]

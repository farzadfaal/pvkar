from django.urls import path

from .views import (
    AddPhoneView,
    PhoneChangePasswordDoneView,
    PhoneChangePasswordView,
    PhoneLoginView,
    PhoneLogoutView,
    PhonePasswordConfirmView,
    PhonePasswordResetCompleteView,
    PhonePasswordResetDoneView,
    PhonePasswordResetView,
    PhoneSignupView,
)

app_name = "accounts"

urlpatterns = [
    path("signup/", PhoneSignupView.as_view(), name="signup"),
    path("login/", PhoneLoginView.as_view(), name="login"),
    path("logout/", PhoneLogoutView.as_view(), name="logout"),
    path("password-reset/", PhonePasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset-done/",
        PhonePasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PhonePasswordConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PhonePasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "change-password/",
        PhoneChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "change-password-done/",
        PhoneChangePasswordDoneView.as_view(),
        name="change_password_done",
    ),
    path(
        "phone/add/",
        AddPhoneView.as_view(),
        name="add_phone",
    ),
]

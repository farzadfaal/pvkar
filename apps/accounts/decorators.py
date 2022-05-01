from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

from . import app_settings

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from .models import User


def role_required(
    function=None,
    redirect_field_name=REDIRECT_FIELD_NAME,
    login_url=None,
    role=User.Roles.contractor,
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.role == role,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def anonymous_required(function=None, redirect_url=app_settings.LOGIN_REDIRECT_URL):
    """Decorator to check if a user is anonymous"""

    if not redirect_url:
        redirect_url = "/"

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous, login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def verified_email_required(
    function=None, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME
):
    """Decorator to check if the user has verified email"""

    def decorator(view_func):
        @login_required(redirect_field_name=redirect_field_name, login_url=login_url)
        def _wrapped_view(request, *args, **kwargs):
            if (
                request.user.is_authenticated
                and request.user.emailaddress_set.filter(is_verified=True).exists()
            ):
                return view_func(request, *args, **kwargs)
            else:
                return redirect("accounts:phone_email_verification")

        return _wrapped_view

    if function:
        return decorator(function)
    return decorator


def verified_phone_required(
    function=None, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME
):
    """Decorator to check if the user has verified phone"""

    def decorator(view_func):
        @login_required(redirect_field_name=redirect_field_name, login_url=login_url)
        def _wrapped_view(request, *args, **kwargs):
            if (
                request.user.is_authenticated
                and request.user.phonenumber_set.filter(is_verified=True).exists()
            ):
                return view_func(request, *args, **kwargs)
            else:
                return redirect("accounts:phone_email_verification")

        return _wrapped_view

    if function:
        return decorator(function)
    return decorator

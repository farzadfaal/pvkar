from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
)
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView

from .mixins import AnonymousRequiredMixin

from . import app_settings
from .forms import (
    AddEmailForm,
    AddPhoneForm,
    PhoneEmailVerificationForm,
    PhoneLoginForm,
    PhoneLogoutForm,
    PhonePasswordResetForm,
    PhoneRegisterForm,
)
from .models import PhoneNumber
from .tokens import phone_token_generator


class PhoneSignupView(AnonymousRequiredMixin, FormView):
    """Display the register form and handle user registration."""

    form_class = PhoneRegisterForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(PhoneSignupView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        if form.errors:
            return render(self.request, self.template_name, context={"form": form})
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhoneLoginView(AnonymousRequiredMixin, LoginView):
    """Display the login form and handle the login action."""

    form_class = PhoneLoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        """Security check complete. Log the user in."""

        user = authenticate(self.request, **form.cleaned_data)
        if user is not None:
            login(self.request, user)
        else:
            form.add_error("login", "Invalid Credentials")
            return render(
                self.request,
                "accounts/login.html",
                context={"form": form},
                status=400,
            )
        return HttpResponseRedirect(self.get_success_url())


class PhoneLogoutView(FormView):
    """Handle logout"""

    template_name = "accounts/logout.html"
    form_class = PhoneLogoutForm
    success_url = _(app_settings.LOGOUT_REDIRECT_URL)

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_logout(self.request)
        return super().form_valid(form)


class PhonePasswordResetView(FormView):
    """Display the password reset form and handle password reset using phone/email."""

    form_class = PhonePasswordResetForm
    template_name = "accounts/password_reset.html"
    success_url = reverse_lazy("accounts:password_reset_done")

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PhonePasswordResetDoneView(PasswordResetDoneView):
    """Renders a template."""

    template_name = "accounts/password_reset_done.html"


class PhonePasswordConfirmView(PasswordResetConfirmView):
    """Accepts `uidb64` and `token` kwargs and validates them.

    If valid, it renders a form for the user to reset the password.
    """

    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class PhonePasswordResetCompleteView(PasswordResetCompleteView):
    """Renders a template"""

    template_name = "accounts/password_reset_complete.html"


class PhoneChangePasswordView(PasswordChangeView):
    """View to change password using old password"""

    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("accounts:change_password_done")


class PhoneChangePasswordDoneView(PasswordChangeDoneView):
    """Renders a template"""

    template_name = "accounts/change_password_done.html"


class AddPhoneView(LoginRequiredMixin, FormView):
    """Add new phone"""

    template_name = "accounts/add_new_phone.html"
    form_class = AddPhoneForm
    success_url = reverse_lazy("accounts:email_verification")

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save(self.request.user)
        if form.errors:
            return render(self.request, self.template_name, context={"form": form})
        return super().form_valid(form)


class AddEmailView(LoginRequiredMixin, FormView):
    """Add new email"""

    template_name = "accounts/add_new_email.html"
    form_class = AddEmailForm
    success_url = reverse_lazy("accounts:email_verification")

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save(self.request.user)
        if form.errors:
            return render(self.request, self.template_name, context={"form": form})
        return super().form_valid(form)

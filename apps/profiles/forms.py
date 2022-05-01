from django import forms

from .models import Profile, Certificate


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user",)


class CertificateModelForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = "__all__"
        exclude = ("profile",)

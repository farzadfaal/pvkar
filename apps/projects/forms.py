from django import forms

from .models import Project


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["service_type"]

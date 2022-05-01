from django import forms

from apps.projects.models import Project

from .models import Building


class BuildingModelForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = "__all__"
        exclude = (
            "employer",
            "status",
        )

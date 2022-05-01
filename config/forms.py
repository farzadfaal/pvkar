from django import forms

from apps.projects.models import Project


class HomeFilterForm(forms.Form):
    category = forms.ChoiceField(choices=Project.Category.choices)

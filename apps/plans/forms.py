from django import forms

from .models import Plan


class BuyCreditForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            "credit",
        ]
        labels = {
            "credit": "میزان اعتبار درخواستی",
        }

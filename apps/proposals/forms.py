from django import forms

from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = "__all__"
        exclude = ("proposer", "project", "completion_time")


class ProposalFormWithTime(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = (
            "proposer",
            "project",
        )

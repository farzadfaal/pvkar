from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages
from apps.accounts.models import PhoneNumber

from apps.projects.models import Project
from apps.subscription.models import Subscription
from apps.buildings.models import Provinces

from .forms import ProposalForm, ProposalFormWithTime
from .models import Proposal


def proposal_detail(request, pk, proposal_pk):
    project = Project.objects.get(pk=pk)
    proposal = Proposal.objects.get(pk=proposal_pk)
    phone_number = PhoneNumber.objects.get(user=proposal.proposer)
    context = {"project": project, "proposal": proposal, "phone_number": phone_number}
    return render(request, "proposals/detail.html", context)


def proposal_detail_employer(request, building_id, project_id, proposal_id):
    context = {}
    proposal = Proposal.objects.get(pk=proposal_id)
    context["proposal"] = proposal
    return render(request, "proposals/proposal_detail_employer.html", context)


def proposal_new(request, pk):
    context = {}
    project = Project.objects.get(pk=pk)
    if project.service_type.startswith("contracting"):
        form = ProposalFormWithTime(request.POST or None)
    else:
        form = ProposalForm(request.POST or None)
    context["form"] = form
    context["project"] = project
    subscription = Subscription.objects.get(user=request.user)

    # Check if project province is Tehran
    if not project.building.province == Provinces.tehran:
        # Check if user has credit for submitting proposal in Tehran-excluded provinces
        if (
            not subscription.unlimited
            and subscription.credit < settings.CONTRACTOR_PROPOSALS_PRICE
        ):
            return render(request, "subscriptions/need_credit.html")
    else:
        # Check if user has credit for submitting proposal in Tehran
        if (
            not subscription.unlimited_tehran
            and subscription.credit < settings.CONTRACTOR_PROPOSALS_TEHRAN_PRICE
        ):
            return render(request, "subscriptions/need_credit.html")

    if request.method == "POST":
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.proposer = request.user
            proposal.project = project
            if not project.building.province == Provinces.tehran:
                if subscription.unlimited:
                    proposal.save()
                else:
                    proposal.proposer = request.user
                    proposal.save()
                    subscription.credit -= settings.CONTRACTOR_PROPOSALS_PRICE
                    subscription.save()
            else:
                if subscription.unlimited_tehran:
                    proposal.save()
                else:
                    proposal.save()
                    subscription.credit -= settings.CONTRACTOR_PROPOSALS_TEHRAN_PRICE
                    subscription.save()
            messages.success(request, "پیشنهاد شما با موفقیت ثبت شد")
            return redirect("projects:project_detail_contractor", project.id)
    return render(request, "proposals/proposal_new.html", context)


def proposal_list_contractor(request):
    proposals = Proposal.objects.filter(proposer=request.user).order_by("-created")
    context = {"proposals": proposals}
    return render(request, "proposals/proposal_list_contractor.html", context)


def proposal_list_employer(request, building_id, project_id):
    context = {}
    proposals = Proposal.objects.filter(project_id=project_id).order_by("-price")
    context["proposals"] = proposals
    return render(request, "proposals/proposal_list_employer.html", context)

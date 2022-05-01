from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from django.conf import settings

from apps.buildings.models import Building, Provinces
from apps.profiles.models import Profile
from apps.subscription.models import Subscription
from apps.accounts.decorators import role_required
from apps.accounts.models import User

from .forms import ProjectModelForm
from .models import Project


@role_required(role=User.Roles.employer)
@require_GET
def project_list(request, building_id):
    context = {}
    projects = Project.objects.filter(building_id=building_id)
    building = Building.objects.get(pk=building_id)
    context["projects"] = projects
    context["building"] = building
    form = ProjectModelForm()
    context["form"] = form
    return render(request, "projects/project_list.html", context)


@role_required(role=User.Roles.employer)
@require_GET
def project_list_employer(request):
    context = {}
    projects = Project.objects.filter(building__employer=request.user)
    context["projects"] = projects
    return render(request, "projects/project_list_employer.html", context)


@role_required(role=User.Roles.contractor)
@require_GET
def project_list_contractor(request):
    context = {}
    profile = Profile.objects.get(user=request.user)
    service_types = list(profile.service_types)
    print(service_types)
    province = profile.province
    projects = Project.objects.filter(service_type__in=service_types)
    context["projects"] = projects
    return render(request, "projects/project_list_contractor.html", context)


@role_required(role=User.Roles.contractor)
@require_GET
def project_detail_contractor(request, pk):
    context = {}
    project = Project.objects.get(pk=pk)
    context["project"] = project
    return render(request, "projects/project_detail_contractor.html", context)


@role_required(role=User.Roles.employer)
@require_http_methods(["GET", "POST"])
def project_new(request, building_id):
    context = {}
    building = Building.objects.get(pk=building_id)
    form = ProjectModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            project = form.save(commit=False)
            project.building = building
            project.save()
            redirect_view = f"{project.service_type}"
            return redirect(
                f"buildings:projects:services:{redirect_view}_new",
                building_id=building.id,
                project_id=form.instance.id,
            )
    context["form"] = form
    context["building"] = building
    return render(request, "projects/project_new.html", context)


@login_required
def project_detail(request, building_id, project_id):
    context = {}
    project = Project.objects.get(pk=project_id)
    context["project"] = project
    return render(request, "projects/project_detail.html", context)


@role_required(role=User.Roles.employer)
@require_GET
def project_finalize(request, building_id, project_id):
    project = Project.objects.get(pk=project_id)
    project.status = Project.Statuses.published
    project.save()
    subscription = Subscription.objects.get(user=request.user)
    if project.building.province == Provinces.tehran:
        subscription.credit -= settings.EMPLOYER_REQUESTS_TEHRAN_PRICE
        subscription.save()
    else:
        subscription.credit -= settings.EMPLOYER_REQUESTS_PRICE
    messages.success(request, "درخواست با موفقیت ثبت و تایید شد.")
    return redirect(
        "buildings:projects:project_detail",
        building_id=building_id,
        project_id=project_id,
    )

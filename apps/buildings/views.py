from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from apps.accounts.decorators import role_required
from apps.accounts.models import User

from .forms import BuildingModelForm
from .models import Building


@role_required(role=User.Roles.employer)
@require_GET
def building_list(request):
    context = {}
    try:
        buildings = Building.objects.filter(employer=request.user)
        context["buildings"] = buildings
    except:
        messages.warning(request, "شما تاکنون ساختمانی ثبت نکرده‌اید")
    form = BuildingModelForm()
    context["form"] = form
    return render(request, "buildings/building_list.html", context)


@role_required(role=User.Roles.employer)
@require_http_methods(["GET", "POST"])
def building_new(request):
    context = {}
    form = BuildingModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            building = form.save(commit=False)
            building.employer = request.user
            building.save()
            return redirect("buildings:building_overview", building_id=form.instance.id)
    context["form"] = form
    return render(request, "buildings/building_new.html", context)


@role_required(role=User.Roles.employer)
@require_GET
def building_overview(request, building_id):
    context = {}
    building = Building.objects.get(pk=building_id)
    context["building"] = building
    return render(request, "buildings/building_overview.html", context)


@role_required(role=User.Roles.employer)
@require_POST
def building_publish(request, building_id):
    building = Building.objects.get(pk=building_id)
    building.status = Building.Statuses.published
    building.save()
    messages.success(request, "ساختمان شما با موفقیت ثبت شد.")
    return redirect("buildings:projects:project_new", building_id=building_id)


@role_required(role=User.Roles.employer)
@require_http_methods(["POST", "GET"])
def building_update(request, building_id):
    context = {}
    building = Building.objects.get(pk=building_id)
    form = BuildingModelForm(request.POST or None, instance=building)
    if request.method == "POST":
        if form.is_valid():
            building = form.save(commit=False)
            building.employer = request.user
            building.save()
            return redirect("buildings:building_overview", building_id=form.instance.id)
    context["form"] = form
    return render(request, "buildings/building_update.html", context)


@role_required(role=User.Roles.employer)
@require_GET
def building_detail(request, building_id):
    context = {}
    building = Building.objects.get(pk=building_id)
    context["building"] = building
    return render(request, "buildings/building_detail.html", context)

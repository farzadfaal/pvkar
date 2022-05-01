from django.shortcuts import render, redirect
from apps.accounts.models import User
from apps.utils.models import StatusModel
from apps.projects.models import Project
from apps.buildings.models import Provinces
from apps.services.models import Category as ServiceTypes
from .forms import HomeFilterForm


def home(request):
    return render(request, "pages/home.html")

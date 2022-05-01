from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from .forms import BuyCreditForm
from .models import Plan


def plan_buy_credit(request):
    context = {}
    form = BuyCreditForm(request.POST or None)
    context["form"] = form
    if request.method == "POST":
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect("plans:plan_detail", pk=form.instance.id)
    return render(request, "plans/buy_credit.html", context)


def plan_detail(request, pk):
    context = {}
    plan = Plan.objects.get(pk=pk)
    if not plan.user == request.user:
        raise PermissionDenied
    context["plan"] = plan
    return render(request, "plans/detail.html", context)


def plan_successful(request, pk):
    return render(request, "plans/successful_payment.html")

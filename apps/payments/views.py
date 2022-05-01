from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.plans.models import Plan

from .gateways.payping import PAYPING_API_KEY, PAYPING_PAY_URL, confirmpay, createpay


def create_pay(request, pk):
    plan = Plan.objects.get(pk=pk)
    return_url = request.build_absolute_uri(
        reverse("payments:confirm_pay", kwargs={"pk": plan.id})
    )
    print(return_url)
    code = createpay(
        amount=1000,
        returnUrl=return_url,
        payer_name=request.user.username,
        payerIdentity=request.user.username,
        description="",
        clientRefId=request.user.id,
    )
    print(code)
    return redirect(PAYPING_PAY_URL + "/gotoipg/" + code)


@csrf_exempt
def confirm_pay(request, pk):

    plan = get_object_or_404(Plan, pk=pk)
    if request.POST:
        # Get data from request
        pay_data = request.POST
        refid = pay_data.get("refid")

        # Confirm Payment
        # All params required*
        amount = 1000
        payment_detail = confirmpay(amount, refid, PAYPING_API_KEY)

        print(payment_detail)

        plan.paid = True
        plan.payment_date = datetime.now()
        plan.save()

        return redirect("plans:successful", pk=plan.id)
    else:
        raise PermissionDenied


def successful_pay(request, pk):
    return render(request, "payments/successful.html")

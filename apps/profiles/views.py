from django.shortcuts import redirect, render

from .forms import CertificateModelForm, ProfileModelForm
from .models import Certificate, Profile


def profile_detail(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, "profiles/profile_detail.html", context)


def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(
        request.POST or None, request.FILES or None, instance=profile
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profiles:profile_detail")
    context = {"profile": profile, "form": form}
    return render(request, "profiles/profile_update.html", context)


def certificate_new(request):
    context = {}
    profile = Profile.objects.get(user=request.user)
    form = CertificateModelForm(
        request.POST or None,
        request.FILES or None,
    )
    if request.method == "POST":
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.profile = profile
            certificate.save()
            return redirect("profiles:certificate_detail", pk=form.instance.id)
    context["form"] = form
    return render(request, "profiles/certificate_new.html", context)


def certificate_detail(request, pk):
    context = {}
    certificate = Certificate.objects.get(pk=pk)
    context["certificate"] = certificate
    return render(request, "profiles/certificate_detail.html", context)


def certificate_list(request):
    context = {}
    certificates = Certificate.objects.filter(
        profile=request.user.profile_set.first().id
    )
    context["certificates"] = certificates
    return render(request, "profiles/certificate_list.html", context)

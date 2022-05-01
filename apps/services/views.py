from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from apps.buildings.models import Building
from apps.projects.models import Project

from .forms import (
    ContractingConcreteServiceModelForm,
    ContractingExcavationServiceModelForm,
    ContractingFacingServiceModelForm,
    ContractingGasServiceModelForm,
    ContractingNailingServiceModelForm,
    ContractingPaintingServiceModelForm,
    ContractingPilingServiceModelForm,
    ContractingPlasteringServiceModelForm,
    ContractingPlumbingServiceModelForm,
    ContractingScaffoldingServiceModelForm,
    ContractingSteelServiceModelForm,
    ContractingTilingServiceModelForm,
    ContractingTrussServiceModelForm,
    ContractingWallServiceModelForm,
    ContractingWaterproofingServiceModelForm,
    ContractingWiringServiceModelForm,
    EngineeringServiceModelForm,
    InsuranceEmployeesLiabilityServiceModelForm,
    InsuranceQualityServiceModelForm,
    InsuranceThirdPartyLiabilityServiceModelForm,
    MaterialAACServiceModelForm,
    MaterialBeamServiceModelForm,
    MaterialClayServiceModelForm,
    MaterialConcreteBlockServiceModelForm,
    MaterialConcreteServiceModelForm,
    MaterialFrameServiceModelForm,
    MaterialGrainsServiceModelForm,
    MaterialPolystyreneServiceModelForm,
)
from .messages import service_new_info, service_success_message
from .models import (
    Category,
    ContractingConcreteService,
    ContractingExcavationService,
    ContractingFacingService,
    ContractingGasService,
    ContractingNailingService,
    ContractingPaintingService,
    ContractingPilingService,
    ContractingPlasteringService,
    ContractingPlumbingService,
    ContractingScaffoldingService,
    ContractingSteelService,
    ContractingTilingService,
    ContractingTrussService,
    ContractingWallService,
    ContractingWaterproofingService,
    ContractingWiringService,
    EngineeringService,
    InsuranceEmployeesLiabilityService,
    InsuranceQualityService,
    InsuranceThirdPartyLiabilityService,
    MaterialAACService,
    MaterialBeamService,
    MaterialClayService,
    MaterialConcreteBlockService,
    MaterialConcreteService,
    MaterialFrameService,
    MaterialGrainsService,
    MaterialPolystyreneService,
)


# Materal Services:: Start
def material_aac_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if not building.employer == request.user:
        raise PermissionDenied
    if project.materialaacservice_set.all:
        context["services"] = MaterialAACService.objects.filter(project=project)
    form = MaterialAACServiceModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_aac
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_aac_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/aac_new.html", context)


def material_aac_delete(request, pk):
    service = MaterialAACService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_aac_new",
        building.id,
        project.id,
    )


def material_beam_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialbeamservice_set.all:
        context["services"] = MaterialBeamService.objects.filter(project=project)
    form = MaterialBeamServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_beam
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_beam_new", building.id, project.id
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/beam_new.html", context)


def material_beam_delete(request, pk):
    service = MaterialBeamService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_beam_new",
        building.id,
        project.id,
    )


def material_clay_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialclayservice_set.all:
        context["services"] = MaterialClayService.objects.filter(project=project)
    form = MaterialClayServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_clay
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_clay_new", building.id, project.id
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/clay_new.html", context)


def material_clay_delete(request, pk):
    service = MaterialClayService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_clay_new",
        building.id,
        project.id,
    )


def material_concrete_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialconcreteservice_set.all:
        context["services"] = MaterialConcreteService.objects.filter(project=project)
    form = MaterialConcreteServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_concrete
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_concrete_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/concrete_new.html", context)


def material_concrete_delete(request, pk):
    service = MaterialConcreteService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_concrete_new",
        building.id,
        project.id,
    )


def material_concrete_block_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialconcreteblockservice_set.all:
        context["services"] = MaterialConcreteBlockService.objects.filter(
            project=project
        )
    form = MaterialConcreteBlockServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_concrete_block
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_concrete_block_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/concrete_block_new.html", context)


def material_concrete_block_delete(request, pk):
    service = MaterialConcreteBlockService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_concrete_block_new",
        building.id,
        project.id,
    )


def material_frame_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialframeservice_set.all:
        context["services"] = MaterialFrameService.objects.filter(project=project)
    form = MaterialFrameServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_frame
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_frame_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/frame_new.html", context)


def material_frame_delete(request, pk):
    service = MaterialFrameService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_frame_new",
        building.id,
        project.id,
    )


def material_grains_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialgrainsservice_set.all:
        context["services"] = MaterialGrainsService.objects.filter(project=project)
    form = MaterialGrainsServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_grains
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_grains_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/grains_new.html", context)


def material_grains_delete(request, pk):
    service = MaterialGrainsService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_grains_new",
        building.id,
        project.id,
    )


def material_polystyrene_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.materialpolystyreneservice_set.all:
        context["services"] = MaterialPolystyreneService.objects.filter(project=project)
    form = MaterialPolystyreneServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.material_polystyrene
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:material_polystyrene_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/material/polystyrene_new.html", context)


def material_polystyrene_delete(request, pk):
    service = MaterialPolystyreneService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:material_polystyrene_new",
        building.id,
        project.id,
    )


# Contracting Services:: Start
def contracting_concrete_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingconcreteservice_set.all:
        context["services"] = ContractingConcreteService.objects.filter(project=project)
    form = ContractingConcreteServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_concrete
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/concrete_new.html", context)


def contracting_concrete_delete(request, pk):
    service = ContractingConcreteService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_concrete_new",
        building.id,
        project.id,
    )


def contracting_excavation_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingexcavationservice_set.all:
        context["services"] = ContractingExcavationService.objects.filter(
            project=project
        )
    form = ContractingExcavationServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_excavation
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/excavation_new.html", context)


def contracting_excavation_delete(request, pk):
    service = ContractingExcavationService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_excavation_new",
        building.id,
        project.id,
    )


def contracting_facing_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingfacingservice_set.all:
        context["services"] = ContractingFacingService.objects.filter(project=project)
    form = ContractingFacingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_facing
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/facing_new.html", context)


def contracting_facing_delete(request, pk):
    service = ContractingFacingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_facing_new",
        building.id,
        project.id,
    )


def contracting_gas_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractinggasservice_set.all:
        context["services"] = ContractingGasService.objects.filter(project=project)
    form = ContractingGasServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_gas
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/gas_new.html", context)


def contracting_gas_delete(request, pk):
    service = ContractingGasService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_gas_new",
        building.id,
        project.id,
    )


def contracting_nailing_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingnailingservice_set.all:
        context["services"] = ContractingNailingService.objects.filter(project=project)
    form = ContractingNailingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_nailing
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/nailing_new.html", context)


def contracting_nailing_delete(request, pk):
    service = ContractingNailingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_nailing_new",
        building.id,
        project.id,
    )


def contracting_painting_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingpaintingservice_set.all:
        context["services"] = ContractingPaintingService.objects.filter(project=project)
    form = ContractingPaintingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_painting
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:contracting_painting_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/painting_new.html", context)


def contracting_painting_delete(request, pk):
    service = ContractingPaintingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_painting_new",
        building.id,
        project.id,
    )


def contracting_piling_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingpilingservice_set.all:
        context["services"] = ContractingPilingService.objects.filter(project=project)
    form = ContractingPilingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_piling
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:contracting_piling_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/piling_new.html", context)


def contracting_piling_delete(request, pk):
    service = ContractingPilingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_piling_new",
        building.id,
        project.id,
    )


def contracting_plastering_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingplasteringservice_set.all:
        context["services"] = ContractingPlasteringService.objects.filter(
            project=project
        )
    form = ContractingPlasteringServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_plastering
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:contracting_plastering_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/plastering_new.html", context)


def contracting_plastering_delete(request, pk):
    service = ContractingPlasteringService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_plastering_new",
        building.id,
        project.id,
    )


def contracting_plumbing_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingplumbingservice_set.all:
        context["services"] = ContractingPlumbingService.objects.filter(project=project)
    form = ContractingPlumbingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_plumbing
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/plumbing_new.html", context)


def contracting_plumbing_delete(request, pk):
    service = ContractingPlumbingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_plumbing_new",
        building.id,
        project.id,
    )


def contracting_scaffolding_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingscaffoldingservice_set.all:
        context["services"] = ContractingScaffoldingService.objects.filter(
            project=project
        )
    form = ContractingScaffoldingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_scaffolding
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/scaffolding_new.html", context)


def contracting_scaffolding_delete(request, pk):
    service = ContractingScaffoldingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_scaffolding_new",
        building.id,
        project.id,
    )


def contracting_steel_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingsteelservice_set.all:
        context["services"] = ContractingSteelService.objects.filter(project=project)
    form = ContractingSteelServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_steel
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/steel_new.html", context)


def contracting_steel_delete(request, pk):
    service = ContractingSteelService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_steel_new",
        building.id,
        project.id,
    )


def contracting_tiling_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingtilingservice_set.all:
        context["services"] = ContractingTilingService.objects.filter(project=project)
    form = ContractingTilingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_tiling
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:contracting_tiling_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/tiling_new.html", context)


def contracting_tiling_delete(request, pk):
    service = ContractingTilingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_tiling_new",
        building.id,
        project.id,
    )


def contracting_truss_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingtrussservice_set.all:
        context["services"] = ContractingTrussService.objects.filter(project=project)
    form = ContractingTrussServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_truss
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/truss_new.html", context)


def contracting_truss_delete(request, pk):
    service = ContractingTrussService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_truss_new",
        building.id,
        project.id,
    )


def contracting_wall_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingwallservice_set.all:
        context["services"] = ContractingWallService.objects.filter(project=project)
    form = ContractingWallServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_wall
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:services:contracting_wall_new",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/wall_new.html", context)


def contracting_wall_delete(request, pk):
    service = ContractingWallService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_wall_new",
        building.id,
        project.id,
    )


def contracting_waterproofing_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingwaterproofingservice_set.all:
        context["services"] = ContractingWaterproofingService.objects.filter(
            project=project
        )
    form = ContractingWaterproofingServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_waterproofing
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/waterproofing_new.html", context)


def contracting_waterproofing_delete(request, pk):
    service = ContractingWaterproofingService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_waterproofing_new",
        building.id,
        project.id,
    )


def contracting_wiring_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.contractingwiringservice_set.all:
        context["services"] = ContractingWiringService.objects.filter(project=project)
    form = ContractingWiringServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.contracting_wiring
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/contracting/wiring_new.html", context)


def contracting_wiring_delete(request, pk):
    service = ContractingWiringService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:contracting_wiring_new",
        building.id,
        project.id,
    )


# Engineering Services:: Start
def engineering_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.engineeringservice_set.all:
        context["services"] = EngineeringService.objects.filter(project=project)
    form = EngineeringServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.engineering
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:engineering_new",
                building.id,
                project.id,
            )
    context["form"] = form
    return render(request, "services/engineering/engineering_new.html", context)


def engineering_delete(request, pk):
    service = EngineeringService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:engineering_new",
        building.id,
        project.id,
    )


def insurance_employee_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.insuranceemployeesliabilityservice_set.all:
        context["services"] = InsuranceEmployeesLiabilityService.objects.filter(
            project=project
        )
    form = InsuranceEmployeesLiabilityServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.insurance_employee
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    context["form"] = form
    return render(request, "services/insurance/employees_new.html", context)


def insurance_employee_delete(request, pk):
    service = InsuranceEmployeesLiabilityService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:insurance_employee_new",
        building.id,
        project.id,
    )


def insurance_third_party_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.insurancethirdpartyliabilityservice_set.all:
        context["services"] = InsuranceThirdPartyLiabilityService.objects.filter(
            project=project
        )
    form = InsuranceThirdPartyLiabilityServiceModelForm(
        request.POST or None, request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.insurance_third_party
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/insurance/third_party_new.html", context)


def insurance_third_party_delete(request, pk):
    service = InsuranceThirdPartyLiabilityService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:insurance_third_party_new",
        building.id,
        project.id,
    )


def insurance_quality_new(request, building_id, project_id):
    building = Building.objects.get(pk=building_id)
    if not building.employer == request.user:
        raise PermissionDenied
    project = Project.objects.get(pk=project_id)
    context = {"project": project, "building": building}
    if project.insurancequalityservice_set.all:
        context["services"] = InsuranceQualityService.objects.filter(project=project)
    form = InsuranceQualityServiceModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.category = Category.insurance_quality
            service.save()
            service_success_message(request)
            return redirect(
                "buildings:projects:project_detail",
                building.id,
                project.id,
            )
    service_new_info(request)
    context["form"] = form
    return render(request, "services/insurance/quality_new.html", context)


def insurance_quality_delete(request, pk):
    service = InsuranceQualityService.objects.get(pk=pk)
    project = service.project
    building = project.building
    service.delete()
    return redirect(
        "buildings:projects:services:insurance_quality_new",
        building.id,
        project.id,
    )

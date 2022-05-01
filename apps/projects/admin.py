from django.contrib import admin

from .models import (
    ContractingProject,
    EngineeringProject,
    InsuranceProject,
    MaterialProject,
)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "building",
        "category",
        "service_type",
    ]


@admin.register(ContractingProject)
class ContractingProjectModelAdmin(ProjectModelAdmin):
    pass


@admin.register(EngineeringProject)
class EngineeringProjectModelAdmin(ProjectModelAdmin):
    pass


@admin.register(InsuranceProject)
class InsuranceProjectModelAdmin(ProjectModelAdmin):
    pass


@admin.register(MaterialProject)
class MaterialProjectModelAdmin(ProjectModelAdmin):
    pass

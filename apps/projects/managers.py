from django.db import models

from .models import Project


class EngineeringProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(category=Project.Category.engineering)
        )


class InsuranceProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(category=Project.Category.insurance)
        )


class MaterialProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(category=Project.Category.material)
        )


class ContractingProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(category=Project.Category.contracting)
        )

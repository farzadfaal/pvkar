from django.db import models
from django_extensions.db.fields import RandomCharField

from apps.services.models import Category as ServiceType
from apps.utils.models import JalaliTimeStampedModel, StatusModel


class Project(JalaliTimeStampedModel, StatusModel):
    class Category(models.TextChoices):
        engineering = "engineering", "خدمات مهندسی"
        insurance = "insurance", "خدمات بیمه"
        material = "material", "خدمات مصالح"
        contracting = "contracting", "خدمات پیمانکاری"

    id = RandomCharField(
        length=6, unique=True, primary_key=True, blank=False, lowercase=True
    )
    building = models.ForeignKey(
        "buildings.Building", on_delete=models.CASCADE, verbose_name="ساختمان"
    )
    # Project category
    category = models.CharField(
        "رسته",
        max_length=11,
        choices=Category.choices,
        null=True,
        help_text="لطفا نوع خدمات مورد نیاز خود را جستجو و انتخاب کنید.",
    )
    # Need Service Type
    service_type = models.CharField(
        "نوع خدمات",
        max_length=25,
        choices=ServiceType.choices,
        null=True,
    )

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست‌ها"

    def __str__(self):
        return f"{self.id} - {self.category}"

    def save(self, *args, **kwargs):
        if self.service_type.startswith(self.Category.engineering):
            self.category = self.Category.engineering
        elif self.service_type.startswith(self.Category.contracting):
            self.category = self.Category.contracting
        elif self.service_type.startswith(self.Category.insurance):
            self.category = self.Category.insurance
        elif self.service_type.startswith(self.Category.material):
            self.category = self.Category.material
        super(Project, self).save(*args, **kwargs)


class EngineeringProject(Project):
    from .managers import EngineeringProjectManager

    objects = EngineeringProjectManager()

    class Meta:
        proxy = True
        verbose_name = "درخواست مهندسی"
        verbose_name_plural = "درخواست‌های مهندسی"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = Project.Category.engineering
        return super().save(*args, **kwargs)


class InsuranceProject(Project):
    from .managers import InsuranceProjectManager

    objects = InsuranceProjectManager()

    class Meta:
        proxy = True
        verbose_name = "درخواست بیمه"
        verbose_name_plural = "درخواست‌های بیمه"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = Project.Category.insurance
        return super().save(*args, **kwargs)


class MaterialProject(Project):
    from .managers import MaterialProjectManager

    objects = MaterialProjectManager()

    class Meta:
        proxy = True
        verbose_name = "درخواست مصالح"
        verbose_name_plural = "درخواست‌های مصالح"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = Project.Category.material
        return super().save(*args, **kwargs)


class ContractingProject(Project):
    from .managers import ContractingProjectManager

    objects = ContractingProjectManager()

    class Meta:
        proxy = True
        verbose_name = "درخواست پیمانکاری"
        verbose_name_plural = "درخواست‌های پیمانکاری"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = Project.Category.contracting
        return super().save(*args, **kwargs)

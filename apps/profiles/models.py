from django.db import models
from multiselectfield import MultiSelectField

from apps.buildings.provinces import Provinces
from apps.projects.models import Project
from apps.services.models import Category as service_types
from apps.accounts.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="کاربر",
        on_delete=models.CASCADE,
    )
    project_types = MultiSelectField(
        "پروژه‌ها",
        choices=Project.Category.choices,
        null=True,
        blank=True,
        max_length=255,
    )
    service_types = MultiSelectField(
        "سرویس‌ها/خدمات",
        choices=service_types.choices,
        null=True,
        blank=True,
        max_length=255,
    )
    province = MultiSelectField(
        "استان محل سکونت",
        max_length=27,
        choices=Provinces.choices,
        help_text="استان محل ساختمان",
    )
    work_experience = models.PositiveIntegerField(
        "سابقه کار مفید", null=True, blank=True
    )

    # Social Media
    instagram = models.URLField("آدرس صفحه‌ی اینستاگرام", null=True, blank=True)
    telegram = models.URLField("آدرس صفحه‌ی تلگرام", null=True, blank=True)

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"

    def __str__(self):
        return f"{self.user}"


class Certificate(models.Model):
    title = models.CharField("عنوان", max_length=255)
    code = models.CharField("کد گواهی", max_length=255, null=True, blank=True)
    issued_by = models.CharField(
        "مرجع صادر کننده", max_length=255, null=True, blank=True
    )
    image = models.ImageField(
        "تصویر گواهی", upload_to="certificates/", null=True, blank=True
    )
    profile = models.ForeignKey(
        Profile, verbose_name="پروفایل", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "گواهی"
        verbose_name_plural = "گواهی‌ها"

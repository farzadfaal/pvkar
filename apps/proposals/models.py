from django.db import models
from django_extensions.db.fields import RandomCharField
from django_extensions.db.models import TimeStampedModel

from apps.projects.models import Project
from apps.accounts.models import User


class Proposal(TimeStampedModel):
    project = models.ForeignKey(Project, verbose_name="پروژه", on_delete=models.CASCADE)
    proposer = models.ForeignKey(
        User, verbose_name="پیمان‌کار", on_delete=models.CASCADE
    )
    price = models.PositiveBigIntegerField(
        "دستمزد پیشنهادی", help_text="به تومان وارد کنید."
    )
    completion_time = models.PositiveSmallIntegerField(
        "مدت زمان تقریبی اجرای پروژه",
        blank=True,
        null=True,
        help_text="به روز وارد کنید.",
    )
    general_description = models.TextField("توضیحات عمومی", blank=True, null=True)
    special_description = models.TextField("توضیحات تخصصی", blank=True, null=True)
    financial_description = models.TextField("شرایط پرداخت", blank=True, null=True)

    class Meta:
        verbose_name = "پیشنهاد"
        verbose_name_plural = "پیشنهاد‌ها"

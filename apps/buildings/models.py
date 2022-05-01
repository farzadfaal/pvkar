from django.db import models

from apps.utils.models import JalaliTimeStampedModel, StatusModel

from .provinces import Provinces


class Building(JalaliTimeStampedModel, StatusModel):
    class Area(models.TextChoices):
        urban = "urban", "شهری"
        industrial = "industrial", "صنعتی"
        rural = "rural", "روستایی"

    title = models.CharField(
        "عنوان ساختمان",
        max_length=255,
        help_text="لطفا برای شناسایی بهتر ساختمان یک عنوان برای ساختمان انتخاب کنید. مثلا: پروژه‌ی ساختمانی ایپک",
    )
    province = models.CharField(
        "استان", max_length=27, choices=Provinces.choices, help_text="استان محل ساختمان"
    )
    city = models.CharField("شهر", max_length=50, help_text="شهر محل ساختمان")
    district = models.CharField(
        "محله",
        max_length=100,
        help_text="محله یا ناحیه ساختمان. مثلا: منطقه ۸، هفت حوض",
    )
    employer = models.ForeignKey(
        "accounts.Employer", on_delete=models.CASCADE, verbose_name="کارفرما"
    )

    class Meta:
        verbose_name = "ساختمان"
        verbose_name_plural = "ساختمان‌ها"

    def __str__(self):
        return self.title

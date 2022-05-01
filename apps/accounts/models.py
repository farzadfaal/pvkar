from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class Roles(models.TextChoices):
        contractor = "contractor", "پیمانکار"
        employer = "employer", "کارفرما"

    role = models.CharField(
        "نقش کاربری", max_length=11, choices=Roles.choices, default=Roles.employer
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Contractor(User):
    from .managers import ContractorModelManager

    objects = ContractorModelManager()

    class Meta:
        proxy = True
        verbose_name = "پیمانکار"
        verbose_name_plural = "پیمانکارها"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.contractor
        return super().save(*args, **kwargs)


class Employer(User):
    from .managers import EmployerModelManager

    objects = EmployerModelManager()

    class Meta:
        proxy = True
        verbose_name = "کارفرما"
        verbose_name_plural = "کارفرما"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.employer
        return super().save(*args, **kwargs)


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique=True, blank=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = "شماره تلفن"
        verbose_name_plural = "شماره تلفن‌ها"

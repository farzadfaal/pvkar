from django.conf import settings
from django.db import models
from django_jalali.db.models import jDateTimeField

from apps.utils.models import JalaliTimeStampedModel


class Plan(JalaliTimeStampedModel):
    user = models.ForeignKey(
        "accounts.User", verbose_name="کاربر", on_delete=models.CASCADE
    )
    credit = models.IntegerField("اعتبار", null=True, blank=True)
    unlimited = models.BooleanField(
        "شامل عضویت نامحدود یکساله شهرستان‌ها", default=False
    )
    unlimited_tehran = models.BooleanField(
        "شامل عضویت نامحدود یکساله تهران", default=False
    )
    price = models.IntegerField("قابل پرداخت", default=0)
    paid = models.BooleanField("پرداخت شده", default=False)
    payment_date = jDateTimeField("تاریخ پرداخت", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.price = 0
        if self.credit:
            self.price += self.credit
        if self.unlimited:
            if self.unlimited_tehran:
                self.price += settings.CONTRACTORS_UNLIMITED_TEHRAN_PRICE
            else:
                self.price += settings.CONTRACTORS_UNLIMITED_PRICE
        return super().save(*args, **kwargs)

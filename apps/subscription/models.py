import datetime

from django.db import models
from django_jalali.db.models import jDateTimeField

from apps.utils.models import JalaliTimeStampedModel


class Subscription(JalaliTimeStampedModel):
    user = models.OneToOneField(
        "accounts.User", verbose_name="کاربر", on_delete=models.CASCADE
    )
    credit = models.IntegerField("اعتبار", null=True, blank=True)
    unlimited = models.BooleanField(
        "شامل عضویت نامحدود یکساله شهرستان‌ها", default=False
    )
    unlimited_tehran = models.BooleanField(
        "شامل عضویت نامحدود یکساله تهران", default=False
    )
    start_date = jDateTimeField("تاریخ شروع عضویت نامحدود", null=True, blank=True)
    expiration_date = jDateTimeField("تاریخ اتمام عضویت نامحدود", null=True, blank=True)
    expired = models.BooleanField("عضویت یکساله منقضی شده", default=False)

    class Meta:
        verbose_name = "اشتراک"
        verbose_name_plural = "اشتراک‌ها"


class UnlimitedSubscriptionTehran(Subscription):
    from .managers import UnlimitedSubscriptionTehranManager

    objects = UnlimitedSubscriptionTehranManager()

    class Meta:
        proxy = True
        verbose_name = "اشتراک نامحدود تهران و سایر استان‌ها"
        verbose_name_plural = "اشتراک‌های نامحدود تهران و سایر استان‌ها"

    def save(self, *args, **kwargs):
        if self.start_date:
            self.unlimited = True
            self.unlimited_tehran = True
            self.expiration_date = self.start_date + datetime.timedelta(days=365)
        return super().save(*args, **kwargs)


class UnlimitedSubscriptionOthers(Subscription):
    from .managers import UnlimitedSubscriptionOthersManager

    objects = UnlimitedSubscriptionOthersManager()

    class Meta:
        proxy = True
        verbose_name = "اشتراک نامحدود سایر استان‌ها"
        verbose_name_plural = "اشتراک‌های نامحدود سایر استان‌ها"

    def save(self, *args, **kwargs):
        if self.start_date:
            self.unlimited = True
            self.expiration_date = self.start_date + datetime.timedelta(days=365)
        return super().save(*args, **kwargs)

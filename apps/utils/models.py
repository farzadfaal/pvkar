from django.db import models

from apps.utils.fields import JalaliAutoCreatedField, JalaliAutoLastModifiedField


class JalaliTimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = JalaliAutoCreatedField("تاریخ عضویت")
    modified = JalaliAutoLastModifiedField("آخرین ویرایش")

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get("update_fields", None)
        if update_fields:
            kwargs["update_fields"] = set(update_fields).union({"modified"})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    class Statuses(models.TextChoices):
        published = "published", "منتشر شده"
        draft = "draft", "چرک‌نویس"

    status = models.CharField(
        "وضعیت", max_length=9, choices=Statuses.choices, default=Statuses.draft
    )

    class Meta:
        abstract = True

from django.db import models


class UnlimitedSubscriptionTehranManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(unlimited=True, unlimited_tehran=True)
        )


class UnlimitedSubscriptionOthersManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(unlimited=True, unlimited_tehran=False)
        )

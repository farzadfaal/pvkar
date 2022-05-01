from django.contrib import admin

from .models import (
    Subscription,
    UnlimitedSubscriptionOthers,
    UnlimitedSubscriptionTehran,
)

admin.site.register(Subscription)
admin.site.register(UnlimitedSubscriptionTehran)
admin.site.register(UnlimitedSubscriptionOthers)

from django.contrib import admin

from .models import Certificate, Profile


admin.site.register(Certificate)


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "province",
        "get_project_types_display",
        "get_service_types_display",
    ]

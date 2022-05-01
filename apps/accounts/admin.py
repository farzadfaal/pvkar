from django.contrib import admin

from .models import Employer, User, Contractor, PhoneNumber


class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "get_role_display",
    ]


@admin.register(Contractor)
class ContractorsModelAdmin(UserModelAdmin):
    pass


@admin.register(Employer)
class EmployerModelAdmin(UserModelAdmin):
    pass


@admin.register(User)
class UsersModelAdmin(UserModelAdmin):
    pass


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    list_display = [
        "user",
        "phone",
    ]

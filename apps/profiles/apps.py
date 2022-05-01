from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.profiles"
    verbose_name = "02. مدیریت پروفایل کاربران"

    def ready(self) -> None:
        import apps.profiles.signals

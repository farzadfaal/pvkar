from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.subscription"
    verbose_name = "03. مدیریت اشتراک کاربران"

    def ready(self) -> None:
        import apps.subscription.signals

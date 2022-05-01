from django.db import models
from django.utils.timezone import now
from django_jalali.db import models as jmodels
from localflavor.ir.forms import IRIDNumberField, IRPostalCodeField


class JalaliAutoCreatedField(jmodels.jDateTimeField):
    """
    A Jalali DateTimeField that automatically populates itself at
    object creation.
    By default, sets editable=False, default=datetime.now.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("editable", False)
        kwargs.setdefault("default", now)
        super().__init__(*args, **kwargs)


class JalaliAutoLastModifiedField(JalaliAutoCreatedField):
    """
    A DateTimeField that updates itself on each save() of the model.
    By default, sets editable=False and default=datetime.now.
    """

    def get_default(self):
        """Return the default value for this field."""
        if not hasattr(self, "_default"):
            self._default = self._get_default()
        return self._default

    def pre_save(self, model_instance, add):
        value = now()
        if add:
            current_value = getattr(model_instance, self.attname, self.get_default())
            if current_value != self.get_default():
                # when creating an instance and the modified date is set
                # don't change the value, assume the developer wants that
                # control.
                value = getattr(model_instance, self.attname)
            else:
                for field in model_instance._meta.get_fields():
                    if isinstance(field, JalaliAutoCreatedField):
                        value = getattr(model_instance, field.name)
                        break
        setattr(model_instance, self.attname, value)
        return value


class IdentityNumberField(models.CharField):
    def formfield(self, **kwargs):
        defaults = {"form_class": IRIDNumberField}
        defaults.update(kwargs)
        return super(models.CharField, self).formfield(**defaults)


class PostalCodeField(models.CharField):
    def formfield(self, **kwargs):
        defaults = {"form_class": IRPostalCodeField}
        defaults.update(kwargs)
        return super(models.CharField, self).formfield(**defaults)

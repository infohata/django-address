import django
from django.db.models.fields.related import ForeignObject

django_version = django.VERSION

is_django2 = django_version >= (2, 0)


def compat_contribute_to_class(self, cls, name, private_only=False):
    if is_django2:
        super(ForeignObject, self).contribute_to_class(cls, name, private_only=private_only) # type: ignore
    else:
        super(ForeignObject, self).contribute_to_class(cls, name, virtual_only=private_only) # type: ignore

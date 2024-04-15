from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Venta

admin.site.register(Venta)
admin.site.unregister(Group)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from kitchen_shop.api.users.models import Customer, Appeal

admin.site.register(Customer)
admin.site.register(Appeal)

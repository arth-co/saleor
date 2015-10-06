from django.contrib import admin

from .models import User, Vendor, Address

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Address)
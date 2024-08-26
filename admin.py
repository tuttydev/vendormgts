from django.contrib import admin
from .models import Vendor, Contract, PerformanceRating, Procurement

admin.site.register(Vendor)
admin.site.register(Contract)
admin.site.register(PerformanceRating)
admin.site.register(Procurement)

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Truck


class TruckResource(resources.ModelResource):

    class Meta:
        model = Truck
        exclude = ('created', 'modified')
        widgets = {
            'expiration': {'format': '%m/%d/%Y %H:%M:%S %p'},
            'approved': {'format': '%m/%d/%Y %H:%M:%S %p'},
        }


class TruckAdmin(ImportExportModelAdmin):
    resource_class = TruckResource


admin.site.register(Truck, TruckAdmin)


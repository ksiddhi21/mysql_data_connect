from django.contrib import admin
from dbconnect_app.models import Vehicle
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("pk","Name","Type")

admin.site.register(Vehicle,VehicleAdmin)
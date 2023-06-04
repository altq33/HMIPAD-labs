from django.contrib import admin

# Register your models here.
from .models import PrecipitationMeasurement, Country, Location, MeasurementSensors, PrecipitationForCountry

admin.site.register(PrecipitationMeasurement)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(MeasurementSensors)
admin.site.register(PrecipitationForCountry)
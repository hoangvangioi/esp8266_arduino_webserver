from django.contrib import admin
from .models import DHT11, Light, Sound, WaterSensor

# Register your models here.


@admin.register(DHT11)
class DHT11Admin(admin.ModelAdmin):
    list_display = "record_id", "temperature", "humidity", "time"
    list_display_links = "record_id", "temperature", "humidity", "time"


@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    list_display = "record_id", "intensity", "time"
    list_display_links = "record_id", "intensity", "time"


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = "record_id", "intensity", "time"
    list_display_links = "record_id", "intensity", "time"


@admin.register(WaterSensor)
class WaterSensorAdmin(admin.ModelAdmin):
    list_display = "record_id", "water_level", "time"
    list_display_links = "record_id", "water_level", "time"
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.


class BaseModels(models.Model):

    record_id = models.AutoField(
        default=0,
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(0)
        ], 
        unique=True, 
        primary_key=True
    )
    
    time = models.DateTimeField(default=datetime.datetime.now) # Time data was recorded

    class Meta:
        abstract = True
        ordering = ["record_id"]
        
        
class DHT11(BaseModels):

    temperature = models.FloatField(
        default=0.0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
    )
    
    humidity = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
    )

    class Meta:
        verbose_name = _("DHT11")
        verbose_name_plural = _("DHT11s")

    def __str__(self):
        return "DHT11 data"


class WaterSensor(BaseModels):
    
    water_level = models.IntegerField()

    class Meta:
        verbose_name = _("Water Sensor")
        verbose_name_plural = _("Water Sensors")

    def __str__(self):
        return "Water Sersor"


class Sound(BaseModels):

    intensity = models.IntegerField()
    
    class Meta:
        verbose_name = _("Sound")
        verbose_name_plural = _("Sounds")

    def __str__(self):
        return "Sound"


class Light(BaseModels):

    intensity = models.IntegerField()
    
    class Meta:
        verbose_name = _("Light")
        verbose_name_plural = _("Lights")

    def __str__(self):
        return "Light"
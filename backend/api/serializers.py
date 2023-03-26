from django.utils import timezone
from rest_framework import serializers
from .models import DHT11, Light, Sound, WaterSensor


class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''
    Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)    
    

class DHT11DataSerializer(serializers.ModelSerializer):
    
    time = DateTimeFieldWihTZ(format='%d-%m-%Y, %H:%M')
    
    class Meta:
        fields = (
            'record_id',
            'temperature',
            'humidity',
            'time',
        )
        model = DHT11


class LightDataSerializer(serializers.ModelSerializer):
    
    time = DateTimeFieldWihTZ(format='%d-%m-%Y, %H:%M')
    
    class Meta:
        fields = (
            'record_id',
            'intensity',
            'time',
        )
        model = Light


class SoundDataSerializer(serializers.ModelSerializer):
    
    time = DateTimeFieldWihTZ(format='%d-%m-%Y, %H:%M')
    
    class Meta:
        fields = (
            'record_id',
            'intensity',
            'time',
        )
        model = Sound
        
        
class WaterSensorDataSerializer(serializers.ModelSerializer):
    
    time = DateTimeFieldWihTZ(format='%d-%m-%Y, %H:%M')
    
    class Meta:
        fields = (
            'record_id',
            'water_level',
            'time',
        )
        model = WaterSensor
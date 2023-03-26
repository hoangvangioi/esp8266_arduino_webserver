import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DHT11, Light, Sound, WaterSensor
from .serializers import DHT11DataSerializer, LightDataSerializer, SoundDataSerializer, WaterSensorDataSerializer


# Create your views here.


class DHT11ListData(APIView):

    def get(self, request):
        queryset = DHT11.objects.all()
        serializer = DHT11DataSerializer(queryset, many=True)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
    def post(self, request):
        # Convert received time from seconds to datetime format
        newDataDict = request.data
        time_seconds = newDataDict['time']
        old_time = datetime.datetime.now().replace(microsecond=0)
        new_time = old_time - datetime.timedelta(seconds=int(time_seconds))
        newDataDict['time'] = new_time.strftime("%Y-%m-%d %H:%M")
        serializer = DHT11DataSerializer(data=newDataDict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

class DHT11LastRecordData(APIView):

    def get(self, request):
        last_record = DHT11.objects.last()
        # If there are no records set record id to zero
        if last_record is None:
            last_record = DHT11()
            last_record.record_id=0
        serializer = DHT11DataSerializer(last_record)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})


class DHT11DataDetail(APIView):

    def get_object(self, pk):
        try:
            return DHT11.objects.get(pk=pk)
        except DHT11.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = DHT11DataSerializer(queryset)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = DHT11DataSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'Access-Control-Allow-Origin': '*'})


class LightListData(APIView):

    def get(self, request):
        queryset = Light.objects.all()
        serializer = LightDataSerializer(queryset, many=True)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
    def post(self, request):
        # Convert received time from seconds to datetime format
        newDataDict = request.data
        time_seconds = newDataDict['time']
        old_time = datetime.datetime.now().replace(microsecond=0)
        new_time = old_time - datetime.timedelta(seconds=int(time_seconds))
        newDataDict['time'] = new_time.strftime("%Y-%m-%d %H:%M")
        
        serializer = LightDataSerializer(data=newDataDict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})


class LightDataDetail(APIView):

    def get_object(self, pk):
        try:
            return Light.objects.get(pk=pk)
        except Light.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = LightDataSerializer(queryset)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = LightDataSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'Access-Control-Allow-Origin': '*'})
    

class SoundListData(APIView):

    def get(self, request):
        queryset = Sound.objects.all()
        serializer = SoundDataSerializer(queryset, many=True)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
    def post(self, request):
        # Convert received time from seconds to datetime format
        newDataDict = request.data
        time_seconds = newDataDict['time']
        old_time = datetime.datetime.now().replace(microsecond=0)
        new_time = old_time - datetime.timedelta(seconds=int(time_seconds))
        newDataDict['time'] = new_time.strftime("%Y-%m-%d %H:%M")
        
        serializer = SoundDataSerializer(data=newDataDict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})


class SoundDataDetail(APIView):

    def get_object(self, pk):
        try:
            return Sound.objects.get(pk=pk)
        except Sound.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SoundDataSerializer(queryset)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SoundDataSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'Access-Control-Allow-Origin': '*'})


class WaterSensorListData(APIView):

    def get(self, request):
        queryset = WaterSensor.objects.all()
        serializer = WaterSensorDataSerializer(queryset, many=True)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
    def post(self, request):
        # Convert received time from seconds to datetime format
        newDataDict = request.data
        time_seconds = newDataDict['time']
        old_time = datetime.datetime.now().replace(microsecond=0)
        new_time = old_time - datetime.timedelta(seconds=int(time_seconds))
        newDataDict['time'] = new_time.strftime("%Y-%m-%d %H:%M")
        
        serializer = WaterSensorDataSerializer(data=newDataDict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})


class WaterSensorDataDetail(APIView):

    def get_object(self, pk):
        try:
            return WaterSensor.objects.get(pk=pk)
        except WaterSensor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = WaterSensorDataSerializer(queryset)
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = WaterSensorDataSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'Access-Control-Allow-Origin': '*'})
from django.urls import path, include
from .views import (
    DHT11ListData, 
    DHT11LastRecordData, 
    DHT11DataDetail,
    LightListData,
    LightDataDetail,
    SoundListData,
    SoundDataDetail,
    WaterSensorListData,
    WaterSensorDataDetail,
)


urlpatterns = [    
    path('dht11/', DHT11ListData.as_view()),
    path('dht11/last/', DHT11LastRecordData.as_view()),
    path('dht11/<int:pk>/', DHT11DataDetail.as_view()),

    path('light/', LightListData.as_view()),
    path('light/<int:pk>/', LightDataDetail.as_view()),

    path('sound/', SoundListData.as_view()),
    path('sound/<int:pk>/', SoundDataDetail.as_view()),

    path('water/', WaterSensorListData.as_view()),
    path('water/<int:pk>/', WaterSensorDataDetail.as_view()),
    
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
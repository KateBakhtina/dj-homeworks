from django.urls import path, include
from measurement.views import SensorCreateGetView, api_view, SensorUpdateGetView, MeasurementCreateView


urlpatterns = [
    path('api/', api_view),
    path('sensors/', SensorCreateGetView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdateGetView.as_view()),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),
]

from django.urls import path
from measurement.views import SensorCreateGetView, SensorUpdateGetView, MeasurementCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('sensors/', SensorCreateGetView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdateGetView.as_view()),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


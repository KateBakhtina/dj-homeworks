# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement

from django.http import FileResponse
from django.conf import settings


def image_view(request, img):
    path = settings.MEDIA_ROOT / 'images' / img
    return FileResponse(open(path, 'rb'))

class SensorCreateGetView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateGetView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return SensorSerializer
        return SensorDetailSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
















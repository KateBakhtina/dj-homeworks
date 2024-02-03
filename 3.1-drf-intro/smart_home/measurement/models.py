from django.db import models
from django.utils import timezone

class Sensor(models.Model):

    name = models.CharField(max_length=48)
    description = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name}: {self.description}'

class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    datetime_measure = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.sensor}: {self.temperature} {self.datetime_measure}'





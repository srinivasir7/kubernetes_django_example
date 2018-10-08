from django.db import models

# Create your models here.

class WeatherReport(models.Model):
    # city name
    city = models.CharField(max_length=255, null=False)
    # weather status
    status = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.city, self.status)
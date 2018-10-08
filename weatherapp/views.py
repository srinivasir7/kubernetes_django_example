from django.shortcuts import render

from rest_framework import generics
from .models import WeatherReport
from .serializers import WeatherReportSerializer
from rest_framework.response import Response
from rest_framework.views import status


class WeatherReportView(generics.ListAPIView):
    """
    Provides a get method handler.
    GET /weather/:city
    """
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer
    def get(self, request, *args, **kwargs):
        try:
            c_weather = self.queryset.get(city=kwargs["city"])
            return Response(WeatherReportSerializer(c_weather).data)
        except WeatherReport.DoesNotExist:
                return Response(
                data={
                    "message": "Weather report for city: {} does not exist".format(kwargs["city"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class HealthCheckView(generics.ListAPIView):
    def get(self, request):
        return Response(
        data={
            "Health Status: Alive"
            },
        status=status.HTTP_200_OK
        )

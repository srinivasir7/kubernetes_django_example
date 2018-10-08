#WeatherApp URLs
from django.urls import path
from .views import WeatherReportView, HealthCheckView

urlpatterns = [
    path('report/<slug:city>/', WeatherReportView.as_view(), name="weather-detail"),
    path('all/', WeatherReportView.as_view(), name="weather-all"),
    path('health-check/', HealthCheckView.as_view(), name="health-check")
    ]
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status as HTTPStatus
from .models import WeatherReport
from .serializers import WeatherReportSerializer

# tests for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_weather_report(city="", status=""):
        if city != "" and status != "":
            WeatherReport.objects.create(city=city, status=status)

    def setUp(self):
        # add test data
        self.create_weather_report("Chicago", "Sunny")
        self.create_weather_report("Boston", "Rainy")
        self.create_weather_report("Seattle", "Windy")



class GetAllCitiesTest(BaseViewTest):

    def test_get_all_cities(self):
        """
        This test ensures that all weather added in the setUp method
        exist when we make a GET request to the weather/all/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("weather-all")
        )
        # fetch the data from db
        expected = WeatherReport.objects.all()
        serialized = WeatherReportSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, HTTPStatus.HTTP_200_OK)
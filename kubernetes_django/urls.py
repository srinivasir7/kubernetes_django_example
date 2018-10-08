"""
kubernetes_django URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Creating the weather endpoints
    path('weather/', include('weatherapp.urls')),
]

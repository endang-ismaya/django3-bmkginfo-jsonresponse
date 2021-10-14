from django.urls import path
from .views import latest_earth_quake, weather_forecast

urlpatterns = [
    path("latest-earthquake", latest_earth_quake, name="app_bmkginfo__leq"),
    path("weather-forecast", weather_forecast, name="app_bmkginfo__leq__wf"),
]

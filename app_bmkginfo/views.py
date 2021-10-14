from django.shortcuts import render
from django.http import JsonResponse
from bmkginfo import LatestEarthQuake, WeatherForecast

# Create your views here.
def latest_earth_quake(request):
    leq = LatestEarthQuake()
    data = {"data": leq.get_data()}

    return JsonResponse(data)


def weather_forecast(request):
    wf = WeatherForecast()
    data = {"data": wf.get_data()}

    return JsonResponse(data)


from weather import Weather
from displayscreen import DisplayScreen
import geolocation
import requests, json
import time

lat, lon = geolocation.get_geo()
weather = Weather(update_every=60, lat=lat, lon=lon)
display = DisplayScreen()

def updater():
    display.update(weather.get_temperature(), weather.get_weather())

weather.add_callback(updater)

while True:
    time.sleep(1)
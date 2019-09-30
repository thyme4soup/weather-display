
from weather import Weather
from displaygraphics import DisplayGraphics
from queue import Queue
import geolocation
import requests, json
import time

lat, lon = geolocation.get_geo()
weather = Weather(update_every=60, lat=lat, lon=lon)
display = DisplayGraphics()

def updater():
    display.update(weather.get_temperature(), weather.get_weather())

# Display specific
actions = Queue()
display.actions = actions
weather.add_callback(updater)
while True:
    while not actions.empty():
        action, *arguments = actions.get()
        action(*arguments)

    time.sleep(0.125)
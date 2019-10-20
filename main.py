
from weather import Weather
from displaypihat import DisplayPiHat
from queue import Queue
import geolocation
import requests, json
import time

lat, lon = geolocation.get_geo()
weather = Weather(update_every=30, city='Boston')
display = DisplayPiHat()

def updater():
    if weather.active:
        display.tz = weather.get_tz()
        display.dt = weather.get_dt()
        display.update(weather.get_temperature(), weather.get_weather())
    else:
        display.update(None, None)

# Display specific
actions = Queue()
display.actions = actions
weather.add_callback(updater)
while True:
    while not actions.empty():
        action, *arguments = actions.get()
        action(*arguments)

    time.sleep(0.125)

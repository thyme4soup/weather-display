
import requests, json
import time, threading
import config


# URLs and key import
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = config.openweather_api_key

# Weather class allows us to track a specific location with a set of callback functions
class Weather:
    def __init__(self, city_name="San Diego", lat=None, lon=None, update_every=60):
        if lat and lon:
            self.url = f'{base_url}appid={api_key}&lat={lat}&lon={lon}'
        else:
            self.url = base_url + "appid=" + api_key + "&q=" + city_name

        self.callbacks = []
        self.update_every = update_every
        self.update()

    def add_callback(self, callback):
        self.callbacks.append(callback)
        self.update(restart=False)

    def update(self, restart=True):
        try:
            self.active = True
            assert(False)
            self.weather = requests.get(self.url).json()
            for callback in self.callbacks:
                callback()
            if restart:
                threading.Timer(self.update_every, self.update).start()
        except:
            self.active = False
            for callback in self.callbacks:
                callback()
            if restart:
                threading.Timer(self.update_every, self.update).start()

    def get_weather_id(self):
        return self.weather['weather'][0]["id"]

    def get_weather(self):
        # https://openweathermap.org/weather-conditions
        i = self.get_weather_id()
        if i < 300:
            return "Thunder"
        elif i < 600:
            return "Rain"
        elif i < 700:
            return "Snow"
        elif i < 800:
            return "Fog"
        elif i == 800:
            return "Clear"
        elif i < 804:
            return "Partly Cloudy"
        else:
            return "Cloudy"

    def get_temperature(self, units="Farenheit"):
        assert(units == "Farenheit" or units == "Celsius")
        kelvin = self.weather['main']['temp']
        if units == "Farenheit":
            return (kelvin - 273.15) * 9/5 + 32
        elif units == "Celsius":
            return kelvin - 273.15

# Testing/Usage
if __name__ == '__main__':

    weather_tracker = Weather(city_name="San Diego", update_every=10)

    def update_display():
        print(weather_tracker.get_weather())
        print(weather_tracker.get_temperature())

    weather_tracker.add_callback(update_display)

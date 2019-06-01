
#import lixie as lix
import math
from displaybase import Display

# Weather is translated into a numeral for use with the lixie library.
# The lixie itself can be modified with weather icons instead of numbers
weather_mapping = {
    "Thunder" : 0,
    "Rain" : 1,
    "Snow" : 2,
    "Fog" : 3,
    "Clear" : 4,
    "Partly Cloudy" : 5,
    "Cloudy" : 6
}

class DisplayScreen(Display):
    def __init__(self):
        Display.__init__(self)
        #lix.begin(3)

    def update_colors(self):
        # This color mapping assumes a farenheit scale for ease
        # (in boston we can approximate temp in F as 0 to 100)
        # We start at blue, shift to green around 50, and reach full red at 100
        capped_temp = min(max(self.temp, 0), 100)
        red_index = (capped_temp - 50) / 50 if capped_temp > 50 else 0
        blue_index = (50 - capped_temp) / 50 if capped_temp < 50 else 0
        green_index = (50 - abs(capped_temp - 50)) / 50
        red = 255 * (red_index ** 2)
        blue = 255 * (blue_index ** 2)
        green = 255 * (green_index ** 2)
        self.color = (red, green, blue)

    def update(self, temperature, weather):
        self.temp = temperature
        self.weather = weather
        self.update_colors()
        self.display()

    def display(self):
        output = int(round(self.temp)) * 10 + weather_mapping.get(self.weather, 0)
        print(f"{output} {self.weather} {self.color}")
        #lix.write(output)
        #lix.color_on(self.color*)


if __name__ == "__main__":

    display = DisplayScreen()

    display.update("Partially Cloudy")
    display.update("Clear")

    print()
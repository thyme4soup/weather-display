#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import json
import time
import urllib
import sys
import datetime
import pytz
from PIL import Image, ImageFont

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

import inkyphat

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
icon_mapping = {
    "Thunder" : "storm",
    "Rain" : "rain",
    "Snow" : "snow",
    "Fog" : "cloudy",
    "Clear" : "sun",
    "Partly Cloudy" : "cloud",
    "Cloudy" : "cloudy"
}

icons = {}
masks = {}
WARNING_TEMP = 80
pressure = 0

# Load our icon files and generate masks
for icon in glob.glob("resources/icon-*.png"):
    icon_name = icon.split("icon-")[1].replace(".png", "")
    icon_image = Image.open(icon)
    icons[icon_name] = icon_image
    masks[icon_name] = inkyphat.create_mask(icon_image)

# Load the built-in FredokaOne font
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

class DisplayPiHat(Display):
    def __init__(self):
        self.temp = 0
        self.weather = "Rain"
        self.tz = 0
        self.dt = 0
        Display.__init__(self)

    def update_colors(self):
        self.color = "Black"

    def update(self, temperature, weather):
        if temperature and weather:
            self.temp = temperature
            self.weather = weather
            self.active = True
        else:
            self.active = False
        self.update_colors()

        try:
            inkyphat.set_colour(self.color)
        except ValueError:
            print('Invalid colour "{}" for V{}\n'.format(self.color, inkyphat.get_version()))
            if inkyphat.get_version() == 2:
                sys.exit(1)
            print('Defaulting to "red"')

        inkyphat.set_border(inkyphat.BLACK)

        # Load our backdrop image
        inkyphat.set_image("resources/backdrop.png")

        # Let's draw some lines!
        inkyphat.line((69, 36, 69, 81)) # Vertical line
        inkyphat.line((31, 35, 184, 35)) # Horizontal top line
        inkyphat.line((69, 58, 174, 58)) # Horizontal middle line
        inkyphat.line((169, 58, 169, 58), 2) # Red seaweed pixel :D

        # And now some text

        dt = (datetime.datetime.now() + datetime.timedelta(seconds=self.tz - 3600)).strftime("%m/%d %H:%M")

        inkyphat.text((36, 12), dt, inkyphat.WHITE, font=font)

        inkyphat.text((72, 34), "T", inkyphat.WHITE, font=font)
        inkyphat.text((92, 34), u"{:.2f}°".format(self.temp), inkyphat.WHITE if self.temp < WARNING_TEMP else inkyphat.RED, font=font)

        inkyphat.text((72, 58), "Active" if self.active else "Disconn", inkyphat.WHITE, font=font)

        # Draw the current weather icon over the backdrop
        if self.weather is not None:
            inkyphat.paste(icons[icon_mapping[self.weather]], (28, 36), masks[icon_mapping[self.weather]])

        else:
            inkyphat.text((28, 36), "?", inkyphat.RED, font=font)

        self.display()

    def display(self):
        inkyphat.show()


if __name__ == "__main__":

    display = DisplayPiHat()

    display.update(75, "Partly Cloudy")
    display.update(75, "Clear")

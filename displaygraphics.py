
from graphics import *
import math
from displaybase import Display

class DisplayGraphics(Display):
    def __init__(self):
        Display.__init__(self)
        self.win = GraphWin("Weather", 500, 100)
        self.win.setBackground("white")
        self.text = Text(Point(250, 50), "00F Clear")
        self.text.setSize(25)
        self.text.draw(self.win)
        self.actions = None

        self.temp = 0

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
        self.color = (int(red), int(green), int(blue))

    def update(self, temperature, weather):
        try:
            self.temp = temperature
            self.weather = weather
            self.update_colors()
            self.display()
        except Exception as e:
            print(e)

    def display(self):
        if self.actions:
            self.actions.put((self.text.setText, f"{int(round(self.temp))}F {self.weather}"))
            self.actions.put((self.text.setTextColor, color_rgb(*self.color)))




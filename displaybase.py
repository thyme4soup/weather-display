
import sys
import time

class Display:

    def __init__(self):
        self.text = ""

    def update(self, temperature, weather):
        self.text = f"{temperature} {weather}"
        self.display()

    def display(self):
        sys.stdout.write("...{:20}\r".format(self.text))
        sys.stdout.flush()


if __name__ == "__main__":

    display = Display()

    display.update("Partially Cloudy")
    display.update("Clear")

    print()
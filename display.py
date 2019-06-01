
import sys
import time

class Display:

    def __init__(self):
        self.text = ""

    def update(self, text):
        self.text = text
        self.display()

    def display(self):
        sys.stdout.write("...{:20}\r".format(self.text))
        sys.stdout.flush()


if __name__ == "__main__":

    display = Display()

    display.update("Partially Cloudy")
    display.update("Clear")

    print()
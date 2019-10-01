#!/bin/bash
cd /home/pi/weather-display/ && /usr/bin/git pull && /usr/bin/pip3 install -r requirements.txt
/usr/bin/python3 /home/pi/weather-display/main.py &

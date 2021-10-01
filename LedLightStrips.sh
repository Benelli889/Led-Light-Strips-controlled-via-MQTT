#! /bin/sh

bash /home/pi/rpi_ws281x/python/examples/bashloop.sh
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python /home/pi/rpi_ws281x/python/examples/LedLightStrips.py

exit 0

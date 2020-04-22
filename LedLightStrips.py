# -*- coding: utf-8 -*-
# sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/MainAnother.py

import os
import time
import paho.mqtt.client as mqtt
from threading import Thread
from MQTT_Client import MqttHandler
from function_library import *

tStartTime = 0
tEndTime = 0

# Main program logic:
if __name__ == '__main__':
    # Process arguments
    opt_parse()
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                              LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    # while True:

    blau
    SetAll(strip, Color(0, 000, 255))

    strip.show()
    time.sleep(10)

    # gruen
    SetAll(strip, Color(000, 255, 000))
    strip.show()
    time.sleep(10)

    # rot
    SetAll(strip, Color(255, 000, 000))
    strip.show()
    time.sleep(10)

    # for i in range(0, 255):
    #    strip.setBrightness(i)
    #    time.sleep(0.2)

    #Aus / schwarz
    SetAll(strip, Color(256, 256, 256))
    strip.show()

    time.sleep(5)

    strip._cleanup()

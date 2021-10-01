# -*- coding: utf-8 -*-
# sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python LedLightStrips.py
#
# https://www.w3schools.com/colors/colors_rgb.asp
#

import os
import time
import paho.mqtt.client as mqtt
from threading import Thread
from MQTT_Client import MqttHandler
from function_library import *
import SunRiseSunSet
import RPi.GPIO as GPIO
from LoggerClass import LoggerClass

Log = LoggerClass()
Log.Configure('/home/pi/rpi_ws281x/python/examples', 'LED_LIGHT_STRIPS')

GPIO.setmode(GPIO.BCM)
GPIORelay = 24
GPIO.setup(GPIORelay, GPIO.OUT)


mqtt = MqttHandler()


def SetLEDStrip(strip, Color):

    # if dark
    # if SunRiseSunSet.SunRiseSunSet() == True:
    SetAll(strip, Color)
    strip.show()


class Switcher(object):
    strip = 0

    def __init__(self, strip):
        self.strip = strip

    def indirect(self, i):
        method_name = 'number_'+str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        print("strip: {}".format(self.strip))
        Log.Msg("strip: {}".format(self.strip))
        return method()

    def number_0(self):
        # Aus (schwarz)
        print("LED Aus")
        SetAll(self.strip, Color(256, 256, 256))
        self.strip.show()
        GPIO.output(GPIORelay, GPIO.LOW)
        print("strip: {}".format(self.strip))
        Log.Msg("0 - LED Aus")
        return True

    def number_1(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # rot
        print("rot")
        Log.Msg("rot")
        SetLEDStrip(self.strip, Color(255, 0, 0))    # red - blue - green
        return True

    def number_2(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # blau
        print("blau")
        Log.Msg("blau")
        SetLEDStrip(self.strip, Color(0, 255, 0))
        return True

    def number_3(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # gruen
        print("green")
        SetLEDStrip(self.strip, Color(0, 0, 255))
        return True

    def number_4(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # orange
        print("orange")
        SetLEDStrip(self.strip, Color(255, 0, 127))
        return True

    def number_5(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # gelb
        print("gelb")
        SetLEDStrip(self.strip, Color(255, 0, 255))
        return True

    def number_6(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # lila
        print("lila")
        SetLEDStrip(self.strip, Color(255, 255, 0))
        return True

    def number_7(self):
        GPIO.output(GPIORelay, GPIO.HIGH)
        # grau
        # print("grau")
        #SetLEDStrip(strip, Color(127, 127, 127))
        while True:
            print("mqtt.ON_MESSAGE_GLOBAL:", mqtt.ON_MESSAGE_GLOBAL)
            Log.Msg("mqtt.ON_MESSAGE_GLOBAL:", mqtt.ON_MESSAGE_GLOBAL)
            print("Calling:  FadeRGB(strip)")
            Log.Msg("mqtt.ON_MESSAGE_GLOBAL:", mqtt.ON_MESSAGE_GLOBAL)
            FadeRGB(strip)
            print("Calling:  FadeInOut(strip, 255, 255, 255)")
            FadeInOut(strip, 255, 255, 255)
            print("Calling:  Cylon(strip, 255, 0, 0, 3, .1, .5)")
            Cylon(strip, 255, 0, 0, 3, .1, .5)
            print("Calling:  Sparkle(strip, 255, 255, 255, 0)")
            Sparkle(strip, 255, 255, 255, 0)
            print("Calling:  SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))")
            SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))
            print("7 fertig")
            if mqtt.ON_MESSAGE_GLOBAL != '7':
                break
        return True


# Main program logic:
if __name__ == '__main__':

    ON_MESSAGE_GLOBAL_K1 = 0xFF

    # Process arguments
    opt_parse()
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,
                              LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

    print("strip: {}".format(strip))
    Log.Msg("strip: {}".format(strip))
    # Intialize the library (must be called once before other functions).
    strip.begin()
    s = Switcher(strip)

    while True:

        # new MQTT message
        if mqtt.ON_MESSAGE_GLOBAL != ON_MESSAGE_GLOBAL_K1:
            print("ON_MESSAGE_GLOBAL: {}".format(
                mqtt.ON_MESSAGE_GLOBAL))
            Log.Msg("ON_MESSAGE_GLOBAL: {}".format(
                mqtt.ON_MESSAGE_GLOBAL))

            s.indirect(int(mqtt.ON_MESSAGE_GLOBAL))
            ON_MESSAGE_GLOBAL_K1 = mqtt.ON_MESSAGE_GLOBAL

            time.sleep(1)

        else:
            pass
            # print("MQTT Message: {} {}".format("undefined:", mqtt.ON_MESSAGE_GLOBAL))

    # for i in range(0, 255):
    #    strip.setBrightness(i)
    #    time.sleep(0.2)

    time.sleep(5)

    strip._cleanup()
    mqtt._stop()
    GPIO.cleanup()

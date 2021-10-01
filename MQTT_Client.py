# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from threading import Thread
from LoggerClass import LoggerClass

Log = LoggerClass()


class MqttHandler(Thread):

    client = mqtt.Client()

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_disconnect = self.on_disconnect
        self.client.led_on = self.led_on
        self.client.led_off = self.led_off
        self.client.get_status = self.get_status

        self.client.connect("192.168.178.105", 1883)
        self.client.subscribe("house/outside/LED-Strips", 1)

        self.ON_MESSAGE_GLOBAL = 0xFF

    def run(self):
        while True:
            self.client.loop()

    def led_on(self):
        self.client.publish("IoT/LED", payload="1")
        print("LED is ON")

    def led_off(self):
        self.client.publish("IoT/LED", payload="2")
        print("LED is OFF")

    def get_status(self):
        self.client.publish("IoT/LED", payload="3")

    def on_connect(self, client, userdata, flags, rc):
        self.client.publish("IoT/LED", "connected")
        print("connected")
        print("client: {}, userdata: {}, flags: {}, rc: {}".format(
            client, userdata, flags, rc))
        Log.Msg("client: {}, userdata: {}, flags: {}, rc: {}".format(
            client, userdata, flags, rc))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        self.client.publish("IoT/LED", payload="3")
        print("subscribed")
        Log.Msg("subscribed")

    def on_publish(self, client, userdata, mid):
        print("message published")

    def on_message(self, client, userdata, message):
        print("message printed to topic")
        print("client: {}, userdata: {}, message.payload: {}, topic: {} qos: {}".format(
            client, userdata, str(message.payload), message.topic, message.qos))
        Log.Msg("client: {}, --userdata: {}, --message.payload: {}, --topic: {} qos: {}".format(
            client, userdata, str(message.payload), message.topic, message.qos))
        #print('message.payload: ', type(message.payload))
        #Log.Msg('message.payload: ', type(message.payload))
        #Log.Msg('(message.payload.decode: ', (message.payload.decode))
        # Log.Msg('(message.payload.decode("utf-8"): ',
        #        (message.payload.decode("utf-8")))

        if ((message.payload.decode("utf-8") in ['0', '1', '2', '3', '4', '5', '6', '7']) or (message.payload.decode("utf-8") in range(0, 8))):
            self.ON_MESSAGE_GLOBAL = message.payload.decode("utf-8")
            Log.Msg('ON_MESSAGE_GLOBAL 0-7: ', self.ON_MESSAGE_GLOBAL)

    def on_disconnect(self, client, userdata, rc):
        print("Client Disconnected")
        Log.Msg("Client Disconnected")

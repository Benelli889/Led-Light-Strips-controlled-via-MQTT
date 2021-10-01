# Led-Light-Strips-controlled-via-MQTT

Led-Light-Strips on/off via MQTT

#crontab -l
   -- changed to --
#sudo crontab -l

@reboot  bash  /home/pi/rpi_ws281x/python/examples/LedLightStrips.sh

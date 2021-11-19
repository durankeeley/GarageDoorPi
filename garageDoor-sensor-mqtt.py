import os
import RPi.GPIO as GPIO
import time

#Report to a MQTT broker
# pip3 install paho-mqtt
import paho.mqtt.publish as publish
Broker = '192.168.1.242'
pub_topic = 'garage/garage-door/status'

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time.sleep(1)

while 1 >= 0:
    time.sleep(1)

    if GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:  #Door Status is Unknown
      publish.single(pub_topic,"moving",hostname=Broker, port=1883,)
      while GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:
             time.sleep(.5)
      else:
        if GPIO.input(16) == GPIO.LOW:  #Door is Closed
          publish.single(pub_topic,"closed",hostname=Broker, port=1883,)
        if GPIO.input(18) == GPIO.LOW:  #Door is Open
          publish.single(pub_topic,"open",hostname=Broker, port=1883,)
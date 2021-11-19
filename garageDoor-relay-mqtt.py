import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)     # sets the pin input/output setting to OUT
GPIO.output(7, GPIO.HIGH)   # sets the pin output to high

# MQTT
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("garage/garage-door/control")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message_received=str(msg.payload.decode("utf-8"))
    if (message_received) == "activate":
        GPIO.output(7, GPIO.LOW)   # turns the first relay switch ON
        time.sleep(.5)             # pauses system for 1/2 second
        GPIO.output(7, GPIO.HIGH)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.242", 1883, 60)

client.loop_forever()

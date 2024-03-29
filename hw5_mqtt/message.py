# import os
# os.system("istats all")
import subprocess
import serial
import time





# XBee setting
serdev = '/dev/tty.usbserial-AC00CNOV'
s = serial.Serial(serdev, 9600)

# s.write("+++".encode())
# char = s.read(2)
# print("Enter AT mode.")
# print(char.decode())

# s.write("ATMY 0x270\r\n".encode())
# char = s.read(3)
# print("Set MY 0x270.")
# print(char.decode())

# s.write("ATDL 0x170\r\n".encode())
# char = s.read(3)
# print("Set DL 0x170.")
# print(char.decode())

# s.write("ATWR\r\n".encode())
# char = s.read(3)
# print("Write config.")
# print(char.decode())

# s.write("ATMY\r\n".encode())
# char = s.read(4)
# print("MY :")
# print(char.decode())

# s.write("ATDL\r\n".encode())
# char = s.read(4)
# print("DL : ")
# print(char.decode())

# s.write("ATCN\r\n".encode())
# char = s.read(3)
# print("Exit AT mode.")

# print(char.decode())

import paho.mqtt.client as paho
import time
mqttc = paho.Client()

# Settings for connection
host = "localhost"
topic= "Mbed"
port = 1883

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)
    


first = True
while True:
    if first:
        line = s.read(13)
        first = False
    else:
        line = s.read(13)
    print('Get:', line.decode())

    mesg = line.decode()
    mqttc.publish(topic, mesg)
    print('Sent:' , mesg)
    time.sleep(1)
    # s.write(fan.encode())
    # line = s.read(20)
    # print('Get:', line.decode())

    # s.write(battery.encode())
    # line = s.read(21)
    # print('Get:', line.decode())

    # s.close()


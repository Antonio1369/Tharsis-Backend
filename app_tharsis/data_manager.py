import serial
import bluetooth
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish

class BluetoothManager:
    def __init__(self, address):
        self.address = address
        #self.mqtt_topic = mqtt_topic

    def read_data(self):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((self.address, 1))
        data = sock.recv(1024)
        #sock.close()
        return data
        # publicar los datos en el tema MQTT
        #publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")

class SerialManager:
    def __init__(self, port, baud_rate, mqtt_topic):
        self.serial = serial.Serial(port=port, baudrate=baud_rate)
        self.mqtt_topic = mqtt_topic

    def read_data(self):
        data = self.serial.readline().decode()
        # publicar los datos en el tema MQTT
        publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")

class PinManager:
    def __init__(self, pin, mode, mqtt_topic):
        self.pin = pin
        self.mode = mode
        self.mqtt_topic = mqtt_topic
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, self.mode)

    def read_data(self):
        data = GPIO.input(self.pin)
        # publicar los datos en el tema MQTT
        publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")

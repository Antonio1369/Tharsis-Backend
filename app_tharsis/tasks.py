#from celery import shared_task
from app_tharsis.data_manager import BluetoothManager, SerialManager, PinManager
#import paho.mqtt.publish as publish

@shared_task
def bluetooth_task():
    bt_manager = BluetoothManager()
    while True:
        data = bt_manager.read_data()
        # publicar los datos en un tema MQTT
#        publish.single("bluetooth_data", payload=data, hostname="broker.example.com")

@shared_task
def serial_task():
    serial_manager = SerialManager()
    while True:
        data = serial_manager.read_data()
        # publicar los datos en un tema MQTT
#        publish.single("serial_data", payload=data, hostname="broker.example.com")

@shared_task
def pin_task():
    pin_manager = PinManager()
    while True:
        data = pin_manager.read_data()
        # publicar los datos en un tema MQTT
#        publish.single("pin_data", payload=data, hostname="broker.example.com")

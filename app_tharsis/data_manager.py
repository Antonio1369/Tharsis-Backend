import serial
import bluetooth
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
from app_tharsis.mpu_acelerometer import MPU6050
import smbus
import numpy as np
import pyrealsense2 as rs



class BluetoothManager:
    def __init__(self, address):
        self.address = address
        self.sock = None

    def read_data(self):
        if self.sock is None:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((self.address, 1))

        try:
            data = self.sock.recv(1024)
            return data
        except bluetooth.btcommon.BluetoothError as e:
            print("Error de conexión: ", e)
            self.sock.close()
            self.sock = None  # restablecer el socket para intentar reconectar
            data = np.random.randint(0, 100, size=1024)  # generar un vector de valores aleatorios
            return data
        # publicar los datos en el tema MQTT
        #publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")

class SerialManager:
    def __init__(self, port, baud_rate, byte_size, paridad, stop_bits):
        self.serial = serial.Serial(port=port, baudrate=baud_rate, bytesize=byte_size, parity=paridad, stopbits=stop_bits, timeout=0.1)
        #self.mqtt_topic = mqtt_topic

    def read_data(self):
        data = self.serial.readline().decode()
        return data
        # publicar los datos en el tema MQTT
        #publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")

class PinManager:
    def __init__(self):
        # start I2C driver
        self.MPU = MPU6050()
        bus = smbus.SMBus(1) # start comm with i2c bus
        gyro_sens,accel_sens = self.MPU.MPU6050_start() # instantiate gyro/accel

    def read_data(self):
        ax,ay,az,wx,wy,wz = self.MPU.mpu6050_conv()
        data = [ax,ay,az,wx,wy,wz]
        return data
        # publicar los datos en el tema MQTT
        #publish.single(self.mqtt_topic, payload=data, hostname="broker.example.com")


class T265Manager:
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.pose)
        self.pipeline.start(self.config)

    def read_data(self):
        while True:
            try:
                frames = self.pipeline.wait_for_frames()
                pose = frames.get_pose_frame()
                if pose:
                    data = pose.get_pose_data()
                    position = data.translation
                    orientation = data.rotation
                    return position, orientation
            except Exception as e:
                print("Error de lectura en la camara: ", e)
                continue

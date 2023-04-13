import serial
import bluetooth
#import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
#from app_tharsis.mpu_acelerometer import MPU6050
#import smbus

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
    def __init__(self, port, baud_rate, byte_size, paridad, stop_bits):
        self.serial = serial.Serial(port=port, baudrate=baud_rate, bytesize=byte_size, parity=paridad, stopbits=stop_bits, timeout=0.1)
        #self.mqtt_topic = mqtt_topic

    def read_data(self):
        MyMPU = self.serial.readline().decode('utf-8').rstrip()
        data = [float(word) for word in MyMPU.split()]
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

class IntelCamera:
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.pose)
        self.pipeline.start(self.config)

    def get_orientation(self):
        frames = self.pipeline.wait_for_frames()
        pose = frames.get_pose_frame()
        if pose:
            data = pose.get_pose_data()
            orientation = [data.rotation.x, data.rotation.y, data.rotation.z, data.rotation.w]
            return orientation
        else:
            return None

    def get_position(self):
        frames = self.pipeline.wait_for_frames()
        pose = frames.get_pose_frame()
        if pose:
            data = pose.get_pose_data()
            position = [data.translation.x, data.translation.y, data.translation.z]
            return position
        else:
            return None

    def __del__(self):
        self.pipeline.stop()


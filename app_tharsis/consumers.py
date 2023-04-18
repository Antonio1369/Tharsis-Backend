from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
import cv2
import numpy
#from asyncio import sleep
#from app_tharsis.data_manager import BluetoothManager, SerialManager, PinManager, T265Manager


class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        #bt = BluetoothManager(address = "EC:94:CB:6F:3F:16" )
        #cam = T265Manager()
        #ser = SerialManager('/dev/ttyUSB0', 115200, 8, 'N', 1)
        #pin = PinManager()
        while True:

            #BLUETOOTH PROCESSING
            #data_bluetooth = bt.read_data()
            #posicion, orientacion = cam.read_data()
            #data_bluetooth = data_bluetooth.decode().split(",")
            #print(data_bluetooth)
            #print(len(data_bluetooth))


            #SERIAL PROCESSING
            #data_serial = ser.read_data()

            #PIN PROCESSING
            #data_pin = pin.read_data()
            self.send(json.dumps({'PPG': randint(0,100),
                                        'oxigeno': randint(0,100),
                                        'BPM' : randint(0,100),
                                        'aceleracion1': randint(0,100),
                                        'aceleracion2': randint(0,100),
                                        'aceleracion3': randint(0,100),
                                        'giroscopio1': randint(0,100),
                                        'giroscopio2': randint(0,100),
                                        'giroscopio3': randint(0,100),

                                        }))

            #if len(data_bluetooth) >1:
            #    await self.send(json.dumps({'value': float(data_bluetooth[1])}))

            sleep(0.08)


class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.accept()
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)
        asyncio.ensure_future(self.send(None))

    async def disconnect(self, close_code):
        self.pipeline.stop()
        await super().disconnect(close_code)

    async def send(self, text_data):
        while True:
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            _, image = cv2.imencode('.jpg', color_image, encode_param)
            await self.send_binary(image.tobytes())


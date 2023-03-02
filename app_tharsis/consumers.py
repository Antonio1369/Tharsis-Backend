from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
from asyncio import sleep
from app_tharsis.data_manager import BluetoothManager, SerialManager, PinManager


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        #bt = BluetoothManager(address = "EC:94:CB:6F:3F:16" )
        #ser = SerialManager('/dev/ttyUSB0', 115200, 8, 'N', 1)
        #pin = PinManager()
        while True:

            #BLUETOOTH PROCESSING
        #    data_bluetooth = bt.read_data()
        #    data_bluetooth = data_bluetooth.decode().split(",")
        #    print(data_bluetooth)
        #    print(len(data_bluetooth))
            
            
            #SERIAL PROCESSING
            #data_serial = ser.read_data()
            #print(data_serial)

            #PIN PROCESSING
            #data_pin = pin.read_data()

            #if len(data_bluetooth) >1 and len(data_serial)>1:
            #    await self.send(json.dumps({'PPG': data_bluetooth[0],
            #                            'oxigeno': data_bluetooth[1],
            #                            'BPM' : data_bluetooth[2],
            #                            'aceleracion': data_serial[0],
            #                            'velocidad': data_serial[2],
            #                            }))
            await self.send(json.dumps({'PPG': randint(1200,1800),
                                        'oxigeno': randint(90,100),
                                        'BPM' : randint(60,80),
                                        'aceleracion': randint(0,100),
                                        'velocidad': randint(0,100),
                                        }))
            
            #if len(data_bluetooth) >1:
            #    await self.send(json.dumps({'value': float(data_bluetooth[1])}))
        
            await sleep(0.8)

    
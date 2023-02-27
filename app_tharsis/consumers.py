from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
from asyncio import sleep
from app_tharsis.data_manager import BluetoothManager, SerialManager, PinManager


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        bt = BluetoothManager(address = "EC:94:CB:6F:3F:16" )
        ser = SerialManager('/dev/ttyUSB1', 115200, 8, 'N', 1)
        pin = PinManager()
        while True:

            #BLUETOOTH PROCESSING
            data_bluetooth = bt.read_data()
            data_bluetooth = data_bluetooth.decode().split(",")
            print(data_bluetooth)
            print(len(data_bluetooth))
            
            
            #SERIAL PROCESSING
            data_serial = ser.read_data()
            print(data_serial)

            #PIN PROCESSING
            #data_pin = pin.read_data()
            await self.send(json.dumps({'PPG': data_bluetooth[0],
                                        'oxigeno': data_bluetooth[1],
                                        'BPM' : data_bluetooth[2],
                                        'aceleracion': data_serial[0],
                                        'velocidad': data_serial[1],
                                        }))
            #await self.send(json.dumps({'PPG': randint(0,100),
            #                            'oxigeno': randint(0,100),
            #                            'BPM' : randint(0,100),
            #                            'aceleracion': randint(0,100),
            #                            'velocidad': randint(0,100),
            #                            }))
            
            #if len(data_bluetooth) >1:
            #    await self.send(json.dumps({'value': float(data_bluetooth[1])}))
        
            await sleep(1)

    
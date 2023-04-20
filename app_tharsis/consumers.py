from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
from asyncio import sleep
import numpy as np
#from app_tharsis.data_manager import BluetoothManager, SerialManager, PinManager
from app_tharsis.data_manager import BluetoothManager



class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        bt = BluetoothManager(address = "EC:94:CB:6F:3F:16" )
        #ser = SerialManager('/dev/ttyUSB0', 115200, 8, 'N', 1)
        #pin = PinManager()
        while True:

            #BLUETOOTH PROCESSING
            data_bluetooth = bt.read_data()
            #print(type(data_bluetooth))
            #print(data_bluetooth)
            if isinstance(data_bluetooth, np.ndarray):
                data_bluetooth = data_bluetooth.tolist()
                #print(data_bluetooth)
            else:
                data_bluetooth =data_bluetooth.decode().split(",")

            
            
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
            
            if len(data_bluetooth) >1:
                await self.send(json.dumps({'PPG': data_bluetooth[0],
                                            'oxigeno': data_bluetooth[1],
                                            'BPM' : data_bluetooth[2],
                                            'aceleracion1': randint(0,100),
                                            'aceleracion2': randint(0,100),
                                            'aceleracion3': randint(0,100),
                                            'giroscopio1': randint(0,100),
                                            'giroscopio2': randint(0,100),
                                            'giroscopio3': randint(0,100),

                                            }))
                
            #if len(data_bluetooth) >1:
            #    await self.send(json.dumps({'value': float(data_bluetooth[1])}))
        
            await sleep(0.08)

    
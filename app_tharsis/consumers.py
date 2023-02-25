from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
from asyncio import sleep
from app_tharsis.data_manager import BluetoothManager


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        bt = BluetoothManager(address = "EC:94:CB:6F:3F:16" )
        while True:
            data = bt.read_data()
            data = str(data.decode())
            print(data)

            await self.send(json.dumps({'value': int(data)}))
            #await self.send(json.dumps({'value2': data}))

        
            await sleep(1)
            


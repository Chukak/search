from channels.generic.websocket import AsyncWebsocketConsumer
#from django.shortcuts import render_to_response
from django.core.serializers import serialize
from .models import Data


import json


class ResultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.number = 0
        await self.accept()
        print('connect')
        self.send(text_data='connect')

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        args = json.loads(text_data)
        print(args)
        text = args.pop('text', None)
        print('receive')
        if text is not None:
            print(Data.objects.search(text, **args)[:5])
            await self.send(serialize("json", Data.objects.search(text,
                                                                  **args)[self.number:self.number + 5]))
            self.number += 5
        else:
            await self.send(serialize("json", []))


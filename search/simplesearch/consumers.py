from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from .models import Data
import json


class ResultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('connect')
        self.send(text_data='connect')
        #await self.close()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        print('receive')
        #kwargs = json.loads(text_data)
        #print(kwargs)
        #text = kwargs.pop('text')
        #context = list(Data.objects.search(text, **kwargs)[:10])
        #await self.send(text_data=serialize('json', context))
        await self.send(text_data='Hello')
        #await self.close()

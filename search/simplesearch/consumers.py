from channels.generic.websocket import WebsocketConsumer
from .models import Data


class ResultConsumer(WebsocketConsumer):
    def connect(self):
        print('connect')
        Data.objects.create(channel_name=self.channel_name)

    def disconnect(self, code):
        Data.objects.filter(channel_name=self.channel_name).delete()

    def search_message(self, event):
        print(event['text'])
        self.send(text_data=event['text'])

from channels.generic.websocket import WebsocketConsumer
from django.core.serializers import serialize
from django.utils.text import force_text
from django.core.serializers.json import DjangoJSONEncoder
from .models import Data
import json
import datetime


class CustomEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            o = o.strftime('%A  %b  %Y  %H:%M')
            return force_text(o)
        return super().default(o)


class ResultConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ''
        self.number = 0
        self.args = {}

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.text = ''
        self.number = 0
        self.args.clear()
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        args = json.loads(text_data)
        action = args.pop('action', '')
        if action != '':
            if action == 'search' and args.get('text', '') != '':
                self.args.clear()
                self.text = args.pop('text', '')
                self.number = 0
                if self.text != '':
                    self.args = args
            if self.number >= 0 and self.args and self.text:
                objects = Data.objects.search(self.text, ranges=(self.number, self.number + 6),
                                              **self.args)
                if objects.count() > 0:
                    self.number += 6
                else:
                    self.number = -1
                self.send(serialize("json", objects,
                                    fields=('text', 'author', 'date_created', 'rating', 'title'),
                                    cls=CustomEncoder))



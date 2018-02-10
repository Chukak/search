from channels.generic.websocket import WebsocketConsumer
from django.core.serializers import serialize
from django.utils.text import force_text
from django.core.serializers.json import DjangoJSONEncoder
from .models import Data
import json
import datetime


# override DjangoJSONEncoder
# for datetime field of data model only
class CustomEncoder(DjangoJSONEncoder):
    def default(self, o):
        # check datetime field
        if isinstance(o, datetime.datetime):
            # set as formatted string
            o = o.strftime('%A  %b  %Y  %H:%M')
            return force_text(o)
        return super().default(o)


# Consumer results
class ResultConsumer(WebsocketConsumer):
    # init with attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ''
        self.number = 0
        self.args = {}

    # connect
    def connect(self):
        self.accept()

    # disconnect
    def disconnect(self, close_code):
        # reset attributes
        self.text = ''
        self.number = 0
        self.args.clear()
        self.close()

    # receive func
    # when socket.send return result as json
    def receive(self, text_data=None, bytes_data=None):
        # parse json object
        args = json.loads(text_data)
        # action
        action = args.pop('action', '')
        if action != '':
            # only search action
            if action == 'search' and args.get('text', '') != '':
                # clear attributes and set text
                self.args.clear()
                self.text = args.pop('text', '')
                self.number = 0
                if self.text != '':
                    self.args = args
            # set ranges for queryset --> queryset.filer()[n: n+6]
            if self.number >= 0 and self.args and self.text:
                # get queryset with parameters
                objects = Data.objects.search(self.text, ranges=(self.number, self.number + 6),
                                              **self.args)
                # if not empty update range for next query
                if objects.count() > 0:
                    self.number += 6
                else:
                    self.number = -1
                # serialize with fields and custom cls to json object, send this
                self.send(serialize("json", objects,
                                    fields=('text', 'author', 'date_created', 'rating', 'title'),
                                    cls=CustomEncoder))



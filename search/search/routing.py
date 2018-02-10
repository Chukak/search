from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
# import Consumer
from simplesearch.consumers import ResultConsumer

# websocket router at path r'^$'
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^$', ResultConsumer)
    ])
})


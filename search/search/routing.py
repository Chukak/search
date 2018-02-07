from django.conf.urls import include
from channels.routing import ProtocolTypeRouter, URLRouter


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        include('simplesearch.routing')
    ])
})

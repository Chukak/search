from django.conf.urls import include, url
from channels.routing import ProtocolTypeRouter, URLRouter
from simplesearch.consumers import ResultConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^$', ResultConsumer),
    ])
})

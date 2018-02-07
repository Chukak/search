from django.conf.urls import url, include
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import ResultConsumer

urlpatterns = ProtocolTypeRouter({
    'websocket': URLRouter([
        url('^$', ResultConsumer)
    ])
})

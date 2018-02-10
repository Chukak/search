from django.conf.urls import url, include


# index url
urlpatterns = [
    url(r'^', include('simplesearch.urls'), name='search'),
]

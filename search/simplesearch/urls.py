from django.conf.urls import url
from .views import SearchView


urlpatterns = [
    # search url
    url(r'^$', SearchView.as_view()),

]

from django.shortcuts import render
import datetime
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from .models import Data
from channels.layers import get_channel_layer
#from redis.client


from django.db.models import Q
# Create your views here.


class SearchView(TemplateView):
    template_name = 'simplesearch/search.html'

    def get(self, request, *args, **kwargs):
        print(get_channel_layer())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        text = self.request.GET.get('search_box', None)
        print(text)
        if text is not None:
            context['objects'] = Data.objects.search(text, **self.request.GET)

        return context

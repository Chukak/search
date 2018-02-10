from django.shortcuts import render, HttpResponse
import datetime
from django.views.generic import TemplateView, View

from django.template.response import TemplateResponse
from .models import Data

#from redis.client
import json


from django.db.models import Q
# Create your views here.


class SearchView(TemplateView):
    template_name = 'simplesearch/search.html'
    template_render_name = 'simplesearch/search_result.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = range(2007, 2018)
        return context

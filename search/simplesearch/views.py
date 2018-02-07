from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Data
from django.db.models import Q
# Create your views here.


class SearchView(TemplateView):
    template_name = 'simplesearch/search.html'

    def get(self, request, *args, **kwargs):
        print(request.GET.get('button', None))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        text = self.request.GET.get('search_box', None)
        if text is not None:
            context['objects'] = Data.objects.search(text, **self.request.GET)
        return context

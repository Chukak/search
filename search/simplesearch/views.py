from django.views.generic import TemplateView


# Template view
class SearchView(TemplateView):
    # template name
    template_name = 'simplesearch/search.html'

    # get years range in template
    # for select tag
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = range(2007, 2018)
        return context

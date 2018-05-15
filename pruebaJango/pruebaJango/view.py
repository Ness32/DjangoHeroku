from django.views.generic import TemplateView
from django.template import loader


class IndexView(TemplateView):
    template_name = 'polls/index.html'

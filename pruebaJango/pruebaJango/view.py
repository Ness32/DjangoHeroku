from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template = loader.get_template('polls/index.html')

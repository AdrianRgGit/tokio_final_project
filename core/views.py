from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View

from content.models import Movie, Serie


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        context['series'] = Serie.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class HistoryView(View):
    template_name = 'core/history.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class StatsView(View):
    template_name = 'core/stats.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

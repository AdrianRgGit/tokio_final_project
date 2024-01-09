from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View

from content.models import Movie, Serie

from .forms import SearchForm


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm(self.request.GET)
        movies = Movie.objects.all()
        series = Serie.objects.all()

        sort_duration = self.request.GET.get('sort_duration')
        sort_release_date = self.request.GET.get('sort_release_date')
        sort_director = self.request.GET.get('sort_director')

        if search_form.is_valid():
            query = search_form.cleaned_data.get('query')
            if query:
                movies = movies.filter(title__icontains=query)
                series = series.filter(title__icontains=query)

        if sort_duration:
            movies = movies.order_by('duration')
            series = series.annotate(num_seasons=Count('season')).order_by('num_seasons')

        if sort_release_date:
            movies = movies.order_by('release_date')
            series = series.order_by('release_date')

        if sort_director:
            movies = movies.order_by('director')
            series = series.order_by('director')

        context['search_form'] = search_form
        context['movies'] = movies
        context['series'] = series
        return context


@method_decorator(login_required, name='dispatch')
class HistoryView(View):
    template_name = 'core/history.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class StatsView(View):
    template_name = 'core/line_chart.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

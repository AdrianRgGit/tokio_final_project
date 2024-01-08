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

        if search_form.is_valid():
            query = search_form.cleaned_data.get('query')
            if query:
                movies = movies.filter(title__icontains=query)
                series = series.filter(title__icontains=query)

        context['search_form'] = search_form
        context['movies'] = movies
        context['series'] = series
        return context


class SearchListView(ListView):
    template_name = 'core/home.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            movies = Movie.objects.filter(title__icontains=query)
            series = Serie.objects.filter(title__icontains=query)
            return {'movies': movies, 'series': series}
        else:
            return {'movies': Movie.objects.none(), 'series': Serie.objects.none()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)  # Añade el formulario al contexto
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

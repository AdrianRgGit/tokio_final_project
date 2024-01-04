from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.base import View
from django.urls import reverse_lazy

from .models import Movie, Serie, Season, Episode

from .forms import MovieForm


@method_decorator(login_required, name='dispatch')
class MovieDetailView(DetailView):
    template_name = "content/movie_detail.html"
    model = Movie


@method_decorator(login_required, name='dispatch')
class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class SerieDetailView(DetailView):
    template_name = "content/serie_detail.html"
    model = Serie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_seasons'] = Season.objects.filter(serie_id=self.object).count()
        return context


@method_decorator(login_required, name='dispatch')
class SeasonListView(ListView):
    model = Season
    template_name = "content/season_list.html"

    def get_queryset(self):
        return Season.objects.filter(serie_id=self.kwargs['pk'])

    # Para cambiar el nombre de object_list a seasons
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = context.pop('object_list')
        return context


@method_decorator(login_required, name='dispatch')
class SeasonDetailView(DetailView):
    template_name = "content/season_detail.html"
    model = Season

    # Para las rutas que necesitan más de 1 pk
    def get_object(self):
        return get_object_or_404(Season, serie_id=self.kwargs['serie_pk'], pk=self.kwargs['season_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_episodes'] = Episode.objects.filter(season_id=self.object).count()
        print("Esto es el context", context['number_episodes'])
        return context


@method_decorator(login_required, name='dispatch')
class EpisodeListView(ListView):
    template_name = "content/episode_list.html"
    model = Episode

    def get_queryset(self):
        return Episode.objects.filter(season_id=self.kwargs['season_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episodes'] = context.pop('object_list')
        return context

    def get_object(self, **kwargs):
        return get_object_or_404(Episode, season_id=self.kwargs['season_pk'], serie_id=self.kwargs['serie_pk'])


@method_decorator(login_required, name='dispatch')
class EpisodeDetailView(DetailView):
    template_name = "content/episode_detail.html"
    model = Episode

    def get_object(self):
        return get_object_or_404(Episode, season_id=self.kwargs['season_pk'],
                                 pk=self.kwargs['episode_pk'])


@method_decorator(login_required, name='dispatch')
class FavoriteMoviesView(View):
    template_name = 'content/favorite_movies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

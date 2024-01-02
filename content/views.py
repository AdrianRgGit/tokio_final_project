from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.base import View
from django.urls import reverse_lazy

from .models import Movie, Serie

from .forms import MovieForm


@method_decorator(login_required, name='dispatch')
class MovieDetailView(DetailView):
    template_name = "content/movie_detail.html"
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('home')


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class SerieDetailView(DetailView):
    template_name = "content/serie_detail.html"
    model = Serie


@method_decorator(login_required, name='dispatch')
class FavoriteMoviesView(View):
    template_name = 'content/favorite_movies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

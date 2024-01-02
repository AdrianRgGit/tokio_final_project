from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView
from django.views.generic.base import View

from .models import Movie, Serie


@method_decorator(login_required, name='dispatch')
class MovieDetailView(DetailView):
    template_name = "content/movie_detail.html"
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ["title", "genre", "director", "duration", "image", "description", "release_date"]


@method_decorator(login_required, name='dispatch')
class SerieDetailView(DetailView):
    template_name = "content/serie_detail.html"
    model = Serie


@method_decorator(login_required, name='dispatch')
class FavoriteMoviesView(View):
    template_name = 'content/favorite_movies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

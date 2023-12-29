from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from content.models import Movie, Serie


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        context['series'] = Serie.objects.all()
        return context


class MovieDetailView(DetailView):
    template_name = "core/movie_detail.html"
    model = Movie


class SerieDetailView(DetailView):
    template_name = "core/serie_detail.html"
    model = Serie


def history(request):
    return render(request, "core/history.html")


def favorite_movies(request):
    return render(request, "core/favorite_movies.html")


@login_required
def profile(request):
    return render(request, "core/profile.html")


def stats(request):
    return render(request, "core/stats.html")


def login(request):
    return render(request, "core/login.html")


def register(request):
    return render(request, "core/register.html")

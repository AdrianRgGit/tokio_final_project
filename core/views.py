from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from content.models import Movie


class HomePageView(ListView):
    template_name = "core/home.html"
    context_object_name = "movies"
    model = Movie


class MovieDetailView(DetailView):
    template_name = "core/movie_detail.html"
    model = Movie


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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "core/home.html")


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

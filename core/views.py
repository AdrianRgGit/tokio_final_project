from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def history(request):
    return render(request, "core/history.html")


def favorite_movies(request):
    return render(request, "core/favorite_movies.html")


def profile(request):
    return render(request, "core/profile.html")


def auth(request):
    return render(request, "core/auth.html")


def stats(request):
    return render(request, "core/stats.html")

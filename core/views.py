from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Home")


def history(request):
    return HttpResponse("History")


def favorite_movies(request):
    return HttpResponse("Favorite-movies")


def profile(request):
    return HttpResponse("Profile")


def auth(request):
    return HttpResponse("Auth")


def stats(request):
    return HttpResponse("Stats")

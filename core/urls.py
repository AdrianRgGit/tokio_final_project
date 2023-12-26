from django.urls import path
from . import views

urlpatterns = [
    # Paths core
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("favorite_movies/", views.favorite_movies, name="favorite_movies"),
    path("profile/", views.profile, name="profile"),
    path("stats/", views.stats, name="stats"),
    path("auth/login", views.login, name="login"),
    path("auth/register", views.register, name="register"),
]

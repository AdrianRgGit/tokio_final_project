from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    # Paths core
    path("", HomePageView.as_view(), name="home"),
    path("history/", views.history, name="history"),
    path("favorite_movies/", views.favorite_movies, name="favorite_movies"),
    path("profile/", views.profile, name="profile"),
    path("stats/", views.stats, name="stats"),
    path("auth/login", views.login, name="login"),
    path("auth/register", views.register, name="register"),
]

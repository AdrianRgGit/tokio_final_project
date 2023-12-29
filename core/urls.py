from django.urls import path
from . import views
from .views import HomePageView, MovieDetailView, SerieDetailView

urlpatterns = [
    # Paths core
    path("", HomePageView.as_view(), name="home"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("serie/<int:pk>/", SerieDetailView.as_view(), name="serie_detail"),
    path("history/", views.history, name="history"),
    path("favorite_movies/", views.favorite_movies, name="favorite_movies"),
    path("profile/", views.profile, name="profile"),
    path("stats/", views.stats, name="stats"),
]

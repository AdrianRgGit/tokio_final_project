from django.urls import path
from . import views
from .views import HomePageView, MovieDetailView, SerieDetailView, HistoryView, FavoriteMoviesView, StatsView

urlpatterns = [
    # Paths core
    path("", HomePageView.as_view(), name="home"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("serie/<int:pk>/", SerieDetailView.as_view(), name="serie_detail"),
    path("history/", HistoryView.as_view(), name="history"),
    path("favorite_movies/", FavoriteMoviesView.as_view(), name="favorite_movies"),
    path("stats/", StatsView.as_view(), name="stats"),
]

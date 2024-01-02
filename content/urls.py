from django.urls import path
from .views import MovieDetailView, SerieDetailView, FavoriteMoviesView, MovieCreateView

urlpatterns = [
    # Paths core
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/create/", MovieCreateView.as_view(), name="create_movie"),
    path("serie/<int:pk>/", SerieDetailView.as_view(), name="serie_detail"),
    path("favorite_movies/", FavoriteMoviesView.as_view(), name="favorite_movies"),
]

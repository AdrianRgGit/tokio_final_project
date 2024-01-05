from django.urls import path
from .views import *

urlpatterns = [
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/create/", MovieCreateView.as_view(), name="create_movie"),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name="update_movie"),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name="delete_movie"),

    path("serie/<int:pk>/", SerieDetailView.as_view(), name="serie_detail"),
    path("serie/create/", SerieCreateView.as_view(), name="create_serie"),
    path('serie/update/<int:pk>/', SerieUpdateView.as_view(), name="update_serie"),
    path('serie/delete/<int:pk>/', SerieDeleteView.as_view(), name="delete_serie"),

    path("serie/<int:pk>/seasons/", SeasonListView.as_view(), name="season_list"),
    path("serie/<int:serie_pk>/seasons/<int:season_pk>/", SeasonDetailView.as_view(), name="season_detail"),
    path("season/create/", SeasonCreateView.as_view(), name="create_season"),
    path('season/update/<int:pk>/', SeasonUpdateView.as_view(), name="update_season"),
    path('season/delete/<int:pk>/', SeasonDeleteView.as_view(), name="delete_season"),

    path("serie/<int:serie_pk>/seasons/<int:season_pk>/episodes", EpisodeListView.as_view(), name="episode_list"),
    path("serie/<int:serie_pk>/seasons/<int:season_pk>/episodes/<int:episode_pk>", EpisodeDetailView.as_view(),
         name="episode_detail"),

    path("favorite_movies/", FavoriteMoviesView.as_view(), name="favorite_movies"),
]

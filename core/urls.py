from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # Paths core
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("favorite_movies/", views.favorite_movies, name="favorite_movies"),
    path("profile/", views.profile, name="profile"),
    path("auth/", views.profile, name="auth"),
    path("stats/", views.profile, name="stats"),

    # Paths admin
    path('admin/', admin.site.urls),
]

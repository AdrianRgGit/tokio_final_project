from django.urls import path
from .views import *

urlpatterns = [
    # Paths core
    path("", HomeView.as_view(), name="home"),
    path('search/', SearchListView.as_view(), name='search'),
    path("history/", HistoryView.as_view(), name="history"),
    path("stats/", StatsView.as_view(), name="stats"),
]

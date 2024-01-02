from django.urls import path
from .views import HomePageView, HistoryView, StatsView

urlpatterns = [
    # Paths core
    path("", HomePageView.as_view(), name="home"),
    path("history/", HistoryView.as_view(), name="history"),
    path("stats/", StatsView.as_view(), name="stats"),
]

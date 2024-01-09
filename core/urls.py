from django.urls import path
from .views import *

urlpatterns = [
    # Paths core
    path("", HomeView.as_view(), name="home"),
    path("history/", HistoryView.as_view(), name="history"),
]

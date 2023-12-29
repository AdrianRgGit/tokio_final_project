from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileView
from . import views

urlpatterns = [
    # El login lo traigo directamente de django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

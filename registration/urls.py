from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileView

urlpatterns = [
    # El login lo traigo directamente de django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

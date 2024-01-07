from django.urls import path
from .views import *

urlpatterns = [
    path("favorite_content/", FavoriteContentView.as_view(), name="favorite_content"),
    path('add_favorite/<str:content_type>/<int:content_id>/', AddFavoriteView.as_view(), name='add_favorite'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("favorite_content/", FavoriteContentView.as_view(), name="favorite_content"),
    path('add_favorite/<str:content_type>/<int:content_id>/', AddFavoriteView.as_view(), name='add_favorite'),
    path('remove_favorite/<str:content_type>/<int:content_id>/', RemoveFavoriteView.as_view(), name='remove_favorite'),

    path("viewed_content/", ViewedContentView.as_view(), name="viewed_content"),
    path('add_viewed/<str:content_type>/<int:content_id>/', ViewedContentView.as_view(), name='add_viewed'),
]

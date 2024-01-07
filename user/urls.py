from django.urls import path
from .views import AddFavoriteView

urlpatterns = [
    path('add_favorite/<str:content_type>/<int:content_id>/', AddFavoriteView.as_view(), name='add_favorite'),
]

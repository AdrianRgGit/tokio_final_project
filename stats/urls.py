from django.urls import path
from .views import *

urlpatterns = [
    path('chart/', FavoriteChartView.as_view(), name='favorite_chart'),
    path('favorites/chart/data/', FavoriteLineChartJSONView.as_view(), name='favorite_chart_data'),

    path('userviewedcontent/chart/', UserViewedContentChartView.as_view(), name='userviewedcontent-chart'),
    path('userviewedcontent/chart/data/', UserViewedContentLineChartJSONView.as_view(),
         name='userviewedcontent-chart-data'),
]

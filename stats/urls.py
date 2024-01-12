from django.urls import path
from .views import *

urlpatterns = [
    path('favorites/chart/', FavoriteChartView.as_view(), name='favorite_chart'),
    path('favorites/chart/data/', FavoriteChartJSONView.as_view(), name='favorite_chart_data'),

    path('user_viewed_content/chart/', UserViewedContentChartView.as_view(), name='user_viewed_content_chart'),
    path('user_viewed_content/chart/data/', UserViewedContentChartJSONView.as_view(),
         name='user_viewed_content_chart_data'),

    path('series_chart/chart/', FavoriteSeriesChartView.as_view(), name='favorites_series_chart'),
    path('favorites_series/chart/data/', FavoriteSeriesChartJSONView.as_view(), name='favorites_series_chart_data'),

    path('user_viewed_series_chart/chart/', UserViewedSeriesChartView.as_view(), name='user_viewed_series_chart'),
    path('user_viewed_series/chart/data/', UserViewedSeriesChartJSONView.as_view(),
         name='user_viewed_series_chart_data'),
]

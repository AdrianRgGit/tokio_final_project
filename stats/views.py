from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from content.models import Movie


def is_admin(user):
    return user.is_authenticated and user.is_staff


@method_decorator(user_passes_test(is_admin), name='dispatch')
class FavoriteChartView(TemplateView):
    template_name = 'stats/chart.html'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class FavoriteLineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        labels = Movie.objects.annotate(favorites_count=Count('favorite')).values_list('title', flat=True)
        return list(labels)

    def get_providers(self):
        """Return names of datasets."""
        return ["Favoritos"]

    def get_data(self):
        """Return dataset to plot."""
        data = Movie.objects.annotate(favorites_count=Count('favorite')).values_list('favorites_count', flat=True)
        return [list(data)]


@method_decorator(user_passes_test(is_admin), name='dispatch')
class UserViewedContentChartView(TemplateView):
    template_name = 'chart.html'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class UserViewedContentLineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        labels = Movie.objects.annotate(view_count=Count('userviewedcontent')).values_list('title', flat=True)
        return list(labels)

    def get_providers(self):
        """Return names of datasets."""
        return ["Vistas"]

    def get_data(self):
        """Return dataset to plot."""
        data = Movie.objects.annotate(view_count=Count('userviewedcontent')).values_list('view_count', flat=True)
        return [list(data)]

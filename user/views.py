from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from content.models import Movie, Serie
from django.views.generic import ListView, TemplateView

from .models import Favorite


@method_decorator(login_required, name='dispatch')
class FavoriteContentView(TemplateView):
    template_name = 'user/favorite_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        favorite_movies = Movie.objects.filter(favorite__user=user)
        favorite_series = Serie.objects.filter(favorite__user=user)

        context['favorite_movies'] = favorite_movies
        context['favorite_series'] = favorite_series

        return context


@method_decorator(login_required, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, content_type, content_id):
        user = request.user

        if content_type == 'movie':
            content_object = get_object_or_404(Movie, pk=content_id)
            Favorite.objects.get_or_create(user=user, movie=content_object)
        elif content_type == 'serie':
            content_object = get_object_or_404(Serie, pk=content_id)
            Favorite.objects.get_or_create(user=user, serie=content_object)
        else:
            return HttpResponseBadRequest("Invalid content type")

        return redirect('favorite_content')

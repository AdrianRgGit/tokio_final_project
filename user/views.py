from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from content.models import Movie, Serie
from .models import Favorite


@method_decorator(login_required, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    @method_decorator(require_POST)
    def post(self, request, content_type, content_id):
        if content_type == 'movie':
            content_object = get_object_or_404(Movie, pk=content_id)
            Favorite.objects.get_or_create(user=request.user, movie_id=content_object)
        elif content_type == 'serie':
            content_object = get_object_or_404(Serie, pk=content_id)
            Favorite.objects.get_or_create(user=request.user, serie_id=content_object)

        return redirect('favorite_movies')

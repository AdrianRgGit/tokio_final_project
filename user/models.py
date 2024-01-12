from django.db import models

from content.models import Movie, Serie
from django.contrib.auth.models import User as DjangoUser


class Like(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.movie:
            return f"{self.user.username}'s Likes movie: {self.movie}"
        else:
            return f"{self.user.username}'s Likes serie: {self.serie}"


class Favorite(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.movie:
            return f"{self.user.username}'s Favorite movie: {self.movie}"
        else:
            return f"{self.user.username}'s Favorite serie: {self.serie}"


class UserViewedContent(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.movie:
            return f"{self.user.username}'s View movie: {self.movie}"
        else:
            return f"{self.user.username}'s View serie: {self.serie}"

from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duration = models.IntegerField()
    image = models.ImageField(upload_to="movies")
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Serie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to="series")
    description = models.TextField()
    release_date = models.DateField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Season(models.Model):
    serie_id = models.ForeignKey(Serie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="seasons")
    description = models.TextField()
    season_number = models.IntegerField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.season_number} - {self.title} - {self.serie_id.title}"


class Episode(models.Model):
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="episodes")
    description = models.TextField()
    duration = models.DurationField()
    episode_number = models.IntegerField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def serie_id(self):
        return self.season_id.serie_id

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.episode_number} - {self.title} - {self.season_id.title} - {self.season_id.serie_id.title}"

from django.contrib import admin
from .models import Movie


class ReadFields(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")


# Register your models here.
admin.site.register(Movie, ReadFields)

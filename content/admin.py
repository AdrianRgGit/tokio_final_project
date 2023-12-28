from django.contrib import admin
from .models import *


class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")


# Register your models here.
admin.site.register(Movie, ReadOnlyFields)
admin.site.register(Serie, ReadOnlyFields)
admin.site.register(Season, ReadOnlyFields)
admin.site.register(Episode, ReadOnlyFields)

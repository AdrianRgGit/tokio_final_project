from django.contrib import admin
from .models import *


class ReadFields(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")


# Register your models here.
admin.site.register(Movie, ReadFields)
admin.site.register(Serie, ReadFields)
admin.site.register(Season, ReadFields)
admin.site.register(Episode, ReadFields)

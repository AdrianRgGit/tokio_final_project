from django.contrib import admin
from .models import *


class ReadFields(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")


# Register your models here.
# admin.site.register(User, ReadFields)
admin.site.register(Like, ReadFields)
admin.site.register(Favorite, ReadFields)
admin.site.register(UserViewedContent, ReadFields)

from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    # Path core
    path('', include("core.urls")),

    # Path admin
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

from core import views

from django.conf import settings

urlpatterns = [
    # Path admin
    path('admin/', admin.site.urls),

    # Path browser reload
    path("__reload__/", include("django_browser_reload.urls")),

    # Path core
    path('', include("core.urls")),

    # Path auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),

    # Path content
    path('content/', include(('content.urls'))),

    # Path user
    path('user/', include(('user.urls'))),

    # Path stats
    path('stats/', include(('stats.urls'))),
]

# Esto se hace para que se puedan ver los ficheros de forma normal sin tener que utlizar producción. Sin esto django no muestra las imágenes en fase de desarrollo.
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

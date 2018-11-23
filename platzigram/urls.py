"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),

        path('', include(('posts.urls', 'posts'), namespace='posts')),
        path('users/', include(('users.urls', 'users'), namespace='users')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

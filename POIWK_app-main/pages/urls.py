from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


from .views import index_view, register_view, login_view, info_view, photo_view, video_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index_view, name='index_view'),
    path('photo/', photo_view, name='photo_view'),
    path('video/', video_view, name='video_view'),
    path('info/', info_view, name='info_view'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
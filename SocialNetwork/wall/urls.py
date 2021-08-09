from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import findUsers

urlpatterns = [
    path('', views.index, name='wall'),
    path('get/ajax/findusers/username', findUsers, name = "find_users")

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
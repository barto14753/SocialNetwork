from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('register', views.register, name ="register"),
    path('login', views.log, name ="login"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
        
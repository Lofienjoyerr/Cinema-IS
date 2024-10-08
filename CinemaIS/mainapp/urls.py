from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie', views.movie_page, name='movie'),
    path('session', views.session_page, name='session')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
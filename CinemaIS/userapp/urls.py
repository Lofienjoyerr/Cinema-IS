from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('reg', views.reg_page, name='reg'),
    path('logout', views.logout_page, name='logout'),
    path('profile', views.profile, name='profile'),
    path('api/admin/get_users', views.get_users_api, name='get_users_api'),
    path('api/admin/get_user', views.get_user_api, name='get_user_api'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='posts/logout.html'), name='logout'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




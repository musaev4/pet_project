"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, update_nft, delete_nft, user_login, user_logout, user_register
from core.views import create_nft

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create_nft/', create_nft, name='create_nft'),
    path('<int:id>/update_nft/', update_nft, name='update_nft'),
    path('<int:id>/delete_nft/', delete_nft, name='delete_nft'),
    path('auth/login/', user_login, name='user_login'),
    path('auth/logout/', user_logout, name='user_logout'),
    path('auth/register/', user_register, name='user_register')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

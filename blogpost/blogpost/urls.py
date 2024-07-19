"""
URL configuration for blogpost project.

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post import views as post_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', post_views.post_list_view, name='home'),  
    path('accounts/', include('user.urls')),  # User app URLs
    path('posts/', include('post.urls')),  # Post app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""zhitu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app01 import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/login/', views.user_login),

    path('user/register/', views.user_register),

    path('admin/home/', views.admin_home),

    path('admin/delete/', views.user_delete),

    path('home/', views.home),

    url(r'^all-(?P<kid>\d+)-(?P<reply_limit>\d+)-(?P<time_limit>\d+)', views.all_tie),  # 按条件搜索帖子

]

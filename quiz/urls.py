"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.view_home_page, name='home'),
    path('test/1', views.view_test1, name='test1'),
    path('test/2', views.view_test2, name='test2'),
    path('test/3', views.view_test3, name='test3'),
    path('test/4', views.view_test4, name='test4'),
    path('test/5', views.view_test5, name='test5'),
    path('final/', views.view_final_page, name='final'),
    path('admin/', admin.site.urls),
]

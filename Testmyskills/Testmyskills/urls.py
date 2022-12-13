"""Testmyskills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from controls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/', views.Login ),
    path('register/', views.registration),
    path('Logout/', views.logout),
    path('About/', views.About),
    path('Contact/', views.Contact),
    path('Test/', views.Test),
    path('level_1', views.level_1),
    path('level_2', views.level_2),
    path('level_3', views.level_3),
    path('level_4', views.level_4),
    path('level_5', views.level_5),

]

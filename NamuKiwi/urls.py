"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from NamuKiwi import views
from django.conf.urls import url

app_name = 'kiwi'

urlpatterns = [
    path('', views.MainPage, name='MainPage'),
    path('create/', views.CreatePage, name='CreatePage'),
    path('<str:page_subject>/', views.DetailPage, name='DetailPage'),
    path('<str:page_subject>/edit/', views.EditPage, name='EditPage'),
    path('<str:page_subject>/delete/', views.DeletePage, name='DeletePage'),
]

"""
URL configuration for NutriDataAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from NutriDataAPI import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('NutriDataAPI/', views.FoodList.as_view(), name='food-list'),
    path('NutriDataAPI/<int:pk>/', views.FoodDetail.as_view(), name='food-detail'),
    path('food/', views.FoodList.as_view(), name='food-list'),
    path('food/<int:pk>/', views.FoodDetail.as_view(), name='food-detail'),
    path('', include('home.urls')),
    path('', include('food.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
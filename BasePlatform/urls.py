from django.contrib import admin
from django.urls import path

import BasePlatform.views as views

app_name = "BasePlatform"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="Home"),
    path('about/', views.About, name="About"),
    path('login/', views.Login, name="Login"),
    path('profile/', views.Profile, name="Profile"),
    path('analysis/', views.Analysis, name="Analysis"),
    path('stockbot/', views.StockBot, name="StockBot"),
]

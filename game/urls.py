from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('allthegames/', views.getAllTheGames),
    path('singlegame/<pk>', views.getSingleGame),
]
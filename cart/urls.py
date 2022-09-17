from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getusercartgames/', views.getUserCartGames),
    path('addgametousercart/', views.addGameToUserCart),
    path('deletefromcart/<pk>', views.deleteGameFromUsersCart),
]

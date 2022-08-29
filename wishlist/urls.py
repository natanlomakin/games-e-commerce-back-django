from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getuserwishlist/', views.showUserWishlistGames),
    path('addtouserwishlist/', views.addGameToUserWishlist),
    path('deltefromuserwishlist/', views.deleteGameFromUserWishlist),


]



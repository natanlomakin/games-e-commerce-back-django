from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getuserwishlist/', views.getUserWishlistGames),
    path('addtouserwishlist/', views.addGameToUserWishlist),
    path('deltefromuserwishlist/<pk>', views.deleteGameFromUserWishlist),
    path('updateuserwishlist/<pk>', views.updateUserWishlist),

]

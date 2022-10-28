from django.urls import path
from . import views

urlpatterns = [
    path('getuserwishlist/', views.getUserWishlistGames),
    path('addtouserwishlist/', views.addGameToUserWishlist),
    path('deltefromuserwishlist/<pk>', views.deleteGameFromUserWishlist),
    path('updateuserwishlist/<pk>', views.updateUserWishlist),

]

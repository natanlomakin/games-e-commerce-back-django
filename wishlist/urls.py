from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('getuserwishlist/', views.getUserWishlistGames),
    path('addtouserwishlist/', views.addGameToUserWishlist),
    path('deltefromuserwishlist/<pk>', views.deleteGameFromUserWishlist),
    path('updateuserwishlist/<pk>', views.updateUserWishlist),

]

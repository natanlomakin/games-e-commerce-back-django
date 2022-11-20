from django.urls import path
from . import views

# A list of paths that are used to access the functions in the views.py file.
urlpatterns = [
    path('getusercartgames/', views.getUserCartGames),
    path('addgametousercart/', views.addGameToUserCart),
    path('deletefromcart/<pk>', views.deleteGameFromUsersCart),
]

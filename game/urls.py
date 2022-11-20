from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('allthegames/', views.getAllTheGames),
    path('singlegame/<pk>', views.getSingleGame),
    path('searchgame/<searchTitle>', views.getGameBySearch),
]
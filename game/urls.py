from django.urls import path
from . import views

urlpatterns = [
    path('allthegames/', views.getAllTheGames),
    path('singlegame/<pk>', views.getSingleGame),
    path('searchgame/<searchTitle>', views.getGameBySearch),
]
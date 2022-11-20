from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import GameSerializer
from .models import Game


@api_view(['GET'])
def getAllTheGames(request):
    """
    Get all the games from the database and return them.
    
    :param request: This is the request that is sent to the server
    :return: A list of all the games in the database.
    """
    allGames = Game.objects.all()
    serializer = GameSerializer(allGames, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleGame(request, pk=-1):
    """
    It takes a request and a primary key, and returns a response containing the serialized data of the
    game with the given primary key
    
    :param request: The request object that was sent to the view
    :param pk: The primary key of the game you want to get
    :return: A single game object
    """
    game = Game.objects.get(_id = pk)
    serializer = GameSerializer(game, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getGameBySearch(request, searchTitle = ""):
    """
    It takes a request and a searchTitle, and returns a response containing a serialized list of games
    that contain the searchTitle in their title
    
    :param request: This is the request object that is sent to the server
    :param searchTitle: The title of the game you want to search for
    :return: A list of games that match the search criteria.
    """
    game = Game.objects.filter(title__contains = searchTitle.title())
    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)
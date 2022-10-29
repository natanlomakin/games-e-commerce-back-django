from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import GameSerializer
from .models import Game


@api_view(['GET'])
def getAllTheGames(request):
    allGames = Game.objects.all()
    serializer = GameSerializer(allGames, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleGame(request, pk=-1):
    game = Game.objects.get(_id = pk)
    serializer = GameSerializer(game, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getGameBySearch(request, searchTitle = ""):
    print(searchTitle.title())
    game = Game.objects.filter(title__contains = searchTitle.title())
    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)
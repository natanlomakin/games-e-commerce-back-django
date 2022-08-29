from dataclasses import dataclass
from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .models import Cart

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCartGames(request):
    cartGames = Cart.objects.filter(user = request.user)
    serializer = CartSerializer(cartGames, many = True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUsersCart(request, pk = -1):
    cartGame = Cart.objects.get(user = request.user, _id = pk)
    cartGame.delete()
    return Response({"deleted":"succesfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserCart(request):
    serializer = CartSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

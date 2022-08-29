from django.db import models
from dataclasses import dataclass
from urllib import request, response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import WishlistSerializer
from .models import Wishlist

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showUserWishlistGames(request, pk = -1):
    wishlistGames = Wishlist.objects.filter(user = request.user)
    serializer = WishlistSerializer(wishlistGames, many = True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUserWishlist(request, pk = -1):    
    wishlistGame = Wishlist.objects.get(user = request.user, _id = pk)
    wishlistGame.delete()
    return Response({"deleted":"succesfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserWishlist(request, pk = -1):
    Wishlist.objects.create(user = request.user, game = request.game)
    return response({"added":"succesfully"})

    """ if request.method == 'POST':
        print(request.game)
        Cart.objects.create(user = request.user, game = request.game)
        return JsonResponse({'POST':"test"}) """
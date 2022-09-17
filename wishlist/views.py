from django.db import models
from dataclasses import dataclass
from urllib import request, response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import WishlistSerializer
from .models import Wishlist


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWishlistGames(request, pk=-1):
    wishlistGames = Wishlist.objects.filter(user=request.user)
    serializer = WishlistSerializer(
        wishlistGames, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUserWishlist(request, pk=-1):
    wishlistGame = Wishlist.objects.filter(user=request.user, _id=pk)
    wishlistGame.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserWishlist(request):
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserWishlist(request, pk=-1):
    currentWishlist = Wishlist.objects.filter(
        user=request.user, _id=pk)
    newWishlist = WishlistSerializer(
        instance=currentWishlist, newWishlist=request.data)
    if newWishlist.is_valid():
        newWishlist.save()
        return Response(newWishlist.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

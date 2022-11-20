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
    """
    It returns a list of all the user's wishlists
    
    :param request: The request object
    :param pk: The primary key of the user
    :return: A list of all the games in the user's wishlist.
    """
    wishlistGames = Wishlist.objects.filter(user=request.user)
    serializer = WishlistSerializer(
        wishlistGames, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUserWishlist(request, pk=-1):
    """
    It deletes a game from a user's wishlist
    
    :param request: The request object
    :param pk: The primary key of the game to be deleted from the user's wishlist
    :return: The response is a status code.
    """
    wishlistGame = Wishlist.objects.filter(user=request.user.id, game=pk)
    wishlistGame.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserWishlist(request):
    """
    It adds a new  wishlist to a user.
    If the serializer is valid, save the data and return a 200 OK response. 
    If the serializer is not valid, return a 404 NOT FOUND response
    
    :param request: The request object
    :return: The response is a status code.
    """
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserWishlist(request, pk=-1):
    """
    It takes a request, and a primary key, and updates the wishlist with the new data
    
    :param request: The request object
    :param pk: The primary key of the wishlist to be updated
    :return: The response is a status code.
    """
    currentWishlist = Wishlist.objects.filter(
        user=request.user, _id=pk)
    newWishlist = WishlistSerializer(
        instance=currentWishlist, newWishlist=request.data)
    if newWishlist.is_valid():
        newWishlist.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

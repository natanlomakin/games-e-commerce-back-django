from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CartSerializer
from .models import Cart


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCartGames(request):
    """
    It returns a list of all the games in the user's cart.
    
    :param request: The request object
    :return: A list of all the games in the user's cart.
    """
    cartGames = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(cartGames, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUsersCart(request, pk=-1):
    """
    It deletes a game from a user's cart.
    
    :param request: The request object
    :param pk: The primary key of the game you want to delete from the cart
    :return: The response is a status code.
    """
    cartGame = Cart.objects.filter(user=request.user.id, game=pk)
    cartGame.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserCart(request):
    """
    It adds a game to a user's cart.
    If the serializer is valid, save the serializer and return a 200 OK response. 
    If the serializer is not valid, return a 404 NOT FOUND response
    
    :param request: The request object
    :return: The response is a status code.
    """
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserCart(request, pk=-1):
    """
    It takes the current cart games of the user and replaces them with the new cart games.
    
    :param request: The request object
    :param pk: The primary key of the cart game you want to update
    :return: The response is a status code.
    """
    currentCartGames = Cart.objects.filter(
        user=request.user, _id=pk)
    newCartGames = CartSerializer(
        instance=currentCartGames, newCartGames=request.data)
    if newCartGames.is_valid():
        newCartGames.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

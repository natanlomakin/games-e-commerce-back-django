from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from order.serializers import OrderSerializer
from django.contrib.auth.models import User
from .models import Order


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserOrder(request):
    """
    It takes the user's request, finds the user's order, serializes the order, and returns the
    serialized data
    
    :param request: The request object is a parameter that's passed to every view in Django. It contains
    metadata about the request, including the HTTP method and the parameters included in the request
    :return: A list of all the orders for the user.
    """
    userOrder = Order.objects.filter(user=request.user)
    serilizer = OrderSerializer(
        userOrder, many=True)
    return Response(serilizer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userOrdering(request):
    """
    It adds an order to a user's orders.
    If the serializer is valid, save the serializer and return a 200 OK response. 
    If the serializer is not valid, return a 404 NOT FOUND response
    
    :param request: The request object
    :return: The response is a serialized object.
    """
    print(request)
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserOrder(request, pk=-1):
    """
    It deletes the order with the given id from the database
    
    :param request: The request object
    :param pk: The primary key of the order you want to delete
    :return: The response is a status code.
    """
    userOrder = Order.objects.get(user=request.user, _id=pk)
    userOrder.delete()
    return Response(status=status.HTTP_200_OK)

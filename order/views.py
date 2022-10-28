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
    userOrder = Order.objects.filter(user=request.user)
    serilizer = OrderSerializer(
        userOrder, many=True)
    return Response(serilizer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userOrdering(request):
    print(request.data)
    serializer = OrderSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserOrder(request, pk=-1):
    userOrder = Order.objects.get(user=request.user, _id=pk)
    userOrder.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

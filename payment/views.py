from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import PaymentSerializer
from .models import PaymentMethod


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserPaymentDetails(request):
    paymentDetails = PaymentMethod.objects.filter(user=request.user)
    serializer = PaymentSerializer(
        paymentDetails, many=True if paymentDetails.length > 1 else False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserPaymentDetails(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserPaymentDetails(request, pk=-1):
    paymentDetail = PaymentMethod.objects.filter(user=request.user, _id=pk)
    paymentDetail.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserPaymentDetaild(request, pk=-1):
    currentPaymentDetails = PaymentMethod.objects.filter(
        user=request.user, _id=pk)
    newPaymentDetails = PaymentSerializer(
        instance=currentPaymentDetails, newPaymentDetails=request.data)
    if newPaymentDetails.is_valid():
        newPaymentDetails.save()
        return Response(newPaymentDetails.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

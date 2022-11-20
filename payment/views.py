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
    """
    It returns a list of payment details for a user if the user has more than one payment method,
    otherwise it returns a single payment method
    
    :param request: The request object
    :return: A list of payment methods for the user.
    """
    paymentDetails = PaymentMethod.objects.filter(user=request.user)
    serializer = PaymentSerializer(
        paymentDetails, many=True if paymentDetails.length > 1 else False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserPaymentDetails(request):
    """
    It adds a payment method to a user.
    If the serializer is valid, save the serializer and return a 200 OK response. 
    If the serializer is not valid, return a 404 NOT FOUND response
    
    :param request: The request object
    :return: The response is a JSON object containing the data that was saved.
    """
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserPaymentDetails(request, pk=-1):
    """
    It deletes a payment method from the database, if the user is the owner of the payment method
    
    :param request: The request object
    :param pk: The primary key of the payment method to delete
    :return: The response is a status code.
    """
    paymentDetail = PaymentMethod.objects.filter(user=request.user, _id=pk)
    paymentDetail.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserPaymentDetaild(request, pk=-1):
    """
    It takes the request, the primary key of the payment method, and updates the payment method with the
    new payment details
    
    :param request: The request object
    :param pk: The primary key of the payment method you want to update
    :return: The response is a status code.
    """
    currentPaymentDetails = PaymentMethod.objects.filter(
        user=request.user, _id=pk)
    newPaymentDetails = PaymentSerializer(
        instance=currentPaymentDetails, newPaymentDetails=request.data)
    if newPaymentDetails.is_valid():
        newPaymentDetails.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile
from .serializers import UserProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    """
    It gets the user profile of the user who is currently logged in and returns it as a response
    
    :param request: The request object.
    :return: A serialized version of the userProfile object.
    """
    userProfile = Profile.objects.get(user=request.user)
    serializer = UserProfileSerializer(userProfile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserProfile(request):
    """
    It adds a new  user profile to a user.
    If the serializer is valid, save the serializer and return a 200 OK response. 
    If the serializer is not valid, return a 404 NOT FOUND response
    
    :param request: The request object
    :return: The response is a status code.
    """
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request, pk=-1):
    """
    It takes a request, and a primary key, and then it updates the user profile with the new data
    
    :param request: The request object
    :param pk: The primary key of the user profile to be updated
    :return: The response is a status code.
    """
    currentUserProfile = Profile.objects.get(
        user=request.user, _id=pk)
    newUserProfile = UserProfileSerializer(
        currentUserProfile, data=request.data)
    if newUserProfile.is_valid():
        newUserProfile.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(newUserProfile.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserProfile(request, pk=-1):
    """
    It deletes a user profile from the database.
    
    :param request: The request object
    :param pk: The primary key of the user profile to delete
    :return: The response is a 200 OK.
    """
    userProfile = Profile.objects.filter(user=request.user.id, _id=pk)
    userProfile.delete()
    return Response(status=status.HTTP_200_OK)

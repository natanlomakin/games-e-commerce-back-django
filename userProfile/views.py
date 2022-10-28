from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile
from .serializers import UserProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    userProfile = Profile.objects.get(user=request.user)
    serializer = UserProfileSerializer(userProfile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserProfile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request, pk=-1):
    currentUserProfile = Profile.objects.filter(
        user=request.user, _id=pk)
    newUserProfile = UserProfileSerializer(
        instance=currentUserProfile, newUserProfile=request.data)
    if newUserProfile.is_valid():
        newUserProfile.save()
        return Response(newUserProfile.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserProfile(request, pk=-1):
    userProfile = Profile.objects.filter(user=request.user.id, _id=pk)
    userProfile.delete()
    return Response(status=status.HTTP_200_OK)

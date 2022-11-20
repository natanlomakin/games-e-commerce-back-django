from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status





@api_view(['POST'])
def registerNewUser(request):
    """
    It creates a new user with the given username, password, email, first name, and last name.
    
    :param request: The request object
    :return: A Response object with a status code of 200 OK.
    """
    User.objects.create_user(username=request.data['username'],
                             password=request.data['password'],
                             email=request.data['email'],
                             first_name=request.data['first_name'],
                             last_name=request.data['last_name'])
    return Response(status=status.HTTP_200_OK)

from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User





@api_view(['POST'])
def registerNewUser(request):
    User.objects.create_user(username=request.data['username'],
                             password=request.data['password'],
                             email=request.data['email'],
                             first_name=request.data['first_name'],
                             last_name=request.data['last_name'])
    return JsonResponse({"register": "Registerd succesfully"}, safe=False)

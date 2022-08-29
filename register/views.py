from dataclasses import dataclass
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.models import User




@api_view(['POST'])
def registerNewUser(request):
    User.objects.create_user(username=request.data['username'],
                             password=request.data['password'],
                             email=request.data['email'],
                             first_name=request.data['first_name'],
                             last_name=request.data['last_name'])
    return JsonResponse({"register": "Registerd succesfully"}, safe=False)

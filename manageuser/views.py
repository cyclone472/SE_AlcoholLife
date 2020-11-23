from django.shortcuts import render
from django.contrib.auth.models import User
from drink.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from manageuser.serializers import *
import json

@api_view(['POST', 'PUT'])
def manage_user(request):
    # create new user
    reqBody = json.loads(request.body)

    if request.method == "POST":
        User.objects.create_user(reqBody['name'], reqBody['email'], reqBody['password'])
        # user = User.objects.create_user(request['name'], request['email'], request['pw'])
    # change user's password
    elif request.method == "PUT":
        u = User.objects.get(username=reqBody['name'])
        u.set_password(reqBody['new_password'])
        u.save()
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from drink.models import *
from manageuser.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from manageuser.serializers import *
import json

@api_view(['POST', 'PUT'])
def manage_user(request):
	# create new user
	reqBody = json.loads(request.body)

	if request.method == "POST":
		User.objects.create_user(reqBody['name'], reqBody['email'], reqBody['password'])
		# user = User.objects.create_user(request['name'], request['email'], request['pw'])
		return Response(status=status.HTTP_200_OK)
	# change user's password
	elif request.method == "PUT":
		u = get_object_or_404(User, username=reqBody['name'])
		u.set_password(reqBody['new_password'])
		u.save()
		return Response(status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def login(request):
	reqBody = json.loads(request.body)
	print(dict(reqBody))
	user = auth.authenticate(request, username=reqBody['name'], 
							password=reqBody['password'])

	if user is not None:
		auth.login(request, user)
		# return redirect('home') 원래는 home.html이든 해서 redirect 필요
		return Response(status=status.HTTP_200_OK)
	else:
		return Response({'error': 'username or password is incorrect'},
						status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def logout(request):
	auth.logout(request)
	# return redirect('home')
	return Response(status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def create_review(request):
	# Create new review
	reqBody = request.data
	cntUser = request.user

	if request.method == "POST":
		Review.objects.create(rating=reqBody['rating'],
			content=reqBody['content'],
			author_id=cntUser.id,
			drink_id=Drink.objects.get(name=reqBody['drink']).id,
			)
		return Response(status=status.HTTP_200_OK)

# get all reviews from particular drink
'''
@api_view(['GET'])
def get_review_for_drink(request):
	target = get_object_or_404(Review, )

'''

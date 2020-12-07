from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from drink.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
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

@api_view(['POST'])
def add_review(request):
	# Create new review
	reqBody = json.loads(request.body)
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

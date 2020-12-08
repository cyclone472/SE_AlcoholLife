from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from drink.models import *
from manageuser.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
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
		return Response({'result' : 'Welcome to Alcohol Life!'},
						status=status.HTTP_200_OK)
	# change user's password
	elif request.method == "PUT":
		u = get_object_or_404(User, username=reqBody['name'])
		u.set_password(reqBody['new_password'])
		u.save()
		return Response({'result' : 'Password change complete.'},
						status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
	reqBody = json.loads(request.body)
	user = auth.authenticate(request, username=reqBody['name'], 
							password=reqBody['password'])
	print(type(user))
	if user is not None:
		token = Token.objects.get_or_create(user=user)
		print(type(token))
		print(token)
		print(token[0])
		print(type(token[0]))
		# return redirect('home') 원래는 home.html이든 해서 redirect 필요
		return Response({'token': str(token[0])}, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'username or password is incorrect'},
						status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
	# 현재 로그인된 유저의 token을 받아와서 삭제
	token = Token.objects.get(user_id=request.user.id)
	token.delete()
	# return redirect('home')
	return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
		review_id = Review.objects.get(content=reqBody['content']).id
		return Response({'review_id' : review_id}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_comment(request):
	print(request.data)
	# Create new comment
	Comment.objects.create(author_id=request.user.id,
			post_id=request.data['review_id'],
			message=request.data['content']
			)
	# Review의 comment_count 숫자 증가
	review = Review.objects.get(id=int(request.data['review_id']))
	review.comment_count = review.comment_count + 1
	review.save()

	return Response(status=status.HTTP_200_OK)

# 내가 쓴 모든 review들 반환
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_review_for_drink(request):
	try:
		qs = Review.objects.filter(author_id=request.user.id)
	except Review.DoesNotExist:
		return Response({'message' : 'Review does not exist.'}, status=status.HTTP_200_OK)

	ret = []
	for review in list(qs.values()):
		drink = Drink.objects.get(id=review['drink_id'])
		category = Category.objects.get(id=drink.category.id)
		elem = {}
		url = 'https://allife-drink.s3.ap-northeast-2.amazonaws.com/{0}/{1}.jpg' \
			  .format(category.name.lower(), drink.image)
		elem['image'] = url
		elem['name'] = drink.name
		ret.append(elem)
	
	return Response({'result' : ret}, status=status.HTTP_200_OK)





























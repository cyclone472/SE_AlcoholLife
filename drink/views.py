from django.shortcuts import render, get_object_or_404
from drink.models import *
from manageuser.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from drink.serializers import *
import csv
import random

# Server 내부에서만 사용되는 함수
def get_url(category, drink_file):
	url = 'https://allife-drink.s3.ap-northeast-2.amazonaws.com/{0}/{1}.jpg' \
		.format(category.lower(), drink_file)
	return url


# Create your views here.
@api_view(['GET'])
def get_item_by_name(request, drink_name):
	print('drink name is : {0}'.format(drink_name))
	target = get_object_or_404(Drink, name=drink_name)
	category = Category.objects.get(id=target.category_id)
	drink_data = DrinkSerializer(target)

	print(type(drink_data.data))
	print(dict(drink_data.data)['name'])
	ret = dict(drink_data.data)
	ret['image'] = get_url(category.name, target.image)
	return Response({'code': status.HTTP_200_OK,
					'result' : ret},
					status=status.HTTP_200_OK)

@api_view(['GET'])
def get_items(request, category):
	cate_id = Category.objects.get(name=category.capitalize())
	try:
		# QuerySet
		qs = Drink.objects.filter(category_id=cate_id)
	except Drink.DoesNotExist:
		return Response({'code': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
	print(list(qs.values())[0])
	# append로 배열의 원소들 중에서 필요한 부분만 추출하기
	ret = []
	for drink in list(qs.values()):
		elem = {}
		elem['name'] = drink['name']
		elem['image'] = get_url(category, drink['image'])
		elem['rating'] = drink['rating']
		elem['ABV'] = drink['ABV']
		ret.append(elem)
	return Response({'code': status.HTTP_200_OK,
					'result' : ret},
					status=status.HTTP_200_OK)

@api_view(['GET'])
def get_reviews_for_drink(request, drink_name):
	drink = get_object_or_404(Drink, name=drink_name)
	drink_data = DrinkSerializer(drink)
	
	try:
		qs = Review.objects.filter(drink_id=drink.id)
	except Review.DoesNotExist:
		return Response({'message': 'Review does not exist.'}, status=status.HTTP_200_OK)
	
	ret = []
	for review in list(qs.values()):
		elem = {}
		author = User.objects.get(id=review['author_id'])
		elem['review_id'] = review['id']
		elem['username'] = author.username
		elem['rating'] = review['rating']
		elem['content'] = review['content']
		elem['comment_count'] = review['comment_count']
		ret.append(elem)
	return Response({'code': status.HTTP_200_OK,
					'result' : ret},
					status=status.HTTP_200_OK)

@api_view(['GET'])
def get_review(request, review_id):
	review = get_object_or_404(Review, id=review_id)
	drink = Drink.objects.get(id=review.drink.id)
	author = User.objects.get(id=review.author.id)

	return Response({'username' : author.username,
					'rating' : review.rating,
					'drink' : drink.name,
					'content' : review.content,
					'comment_count' : review.comment_count},
					status=status.HTTP_200_OK)

@api_view(['POST'])
def add_category(request):
	new_post1 = Category.objects.create(name='Soju')
	new_post2 = Category.objects.create(name='Beer')
	new_post3 = Category.objects.create(name='Makgeolli')


@api_view(['POST'])
def add_drink(request):
	CSV_PATH = ['./makgeolli.csv', './beer.csv']
	for path in CSV_PATH:
		with open(path, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				"""
				print(row)
				Drink.objects.create(
					name = row['이름'],
					ABV = row['도수'],
					capacity = row['용량'],
					company = row['회사'],
					category_id = Category.objects.get(name='Makgeolli').id
				)"""
				instance = Drink.objects.get(name=row['이름'])
				instance.image = row['이미지']
				instance.save()
	print('SUCCESS!')
	return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def add_rating(request):
	qs = Drink.objects.all()

	# for drink in list(qs.values()):
	for drink in qs:
		print(type(drink))
		print(drink)
		drink.rating = random.randrange(4, 10) / 2
		drink.save()
	return Response({'result' : 'SUCCESS!'},
					status=status.HTTP_200_OK)



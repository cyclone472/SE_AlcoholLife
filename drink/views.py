from django.shortcuts import render, get_object_or_404
from drink.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from drink.serializers import *

# Create your views here.
@api_view(['GET'])
def get_item_by_name(request, drink_name):
	print('drink name is : {0}'.format(drink_name))
	target = get_object_or_404(Drink, name=drink_name)
	drink_data = DrinkSerializer(target)

	url = 'https://allife-drink.s3.ap-northeast-2.amazonaws.com/{0}/{1}.jpg' \
		.format(type, drink_name)
	return Response({'code': status.HTTP_200_OK,
					'result' : drink_data.data,
					'image' : url},
					status=status.HTTP_200_OK)

@api_view(['POST'])
def add_category(request):
	new_post1 = Category.objects.create(name='Soju')
	new_post2 = Category.objects.create(name='Beer')
	new_post3 = Category.objects.create(name='Makgeolli')

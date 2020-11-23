from django.shortcuts import render, get_object_or_404
from drink.models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from drink.serializers import *

# Create your views here.
@api_view(['GET'])
def get_item_by_name(request, type, drink_name):
	print('drink name is : {0}'.format(drink_name))
	if type == 'soju':
		target = get_object_or_404(Soju, name=drink_name)
		drink_data = SojuSerializer(target)
	elif type == 'beer':
		target = get_object_or_404(Beer, name=drink_name)
		drink_data = BeerSerializer(target)
	elif type == 'makgeolli':
		target = get_object_or_404(Makgeolli, name=drink_name)
		drink_data = MakgeolliSerializer(target)

	print('how can i do this?')
	return Response({'code': status.HTTP_200_OK,
					'result' : drink_data.data},
					status=status.HTTP_200_OK)

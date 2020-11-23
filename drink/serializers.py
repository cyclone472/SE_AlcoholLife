from rest_framework import serializers
# from .models import Post
from drink.models import *
from django.contrib.auth.models import User

class SojuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Soju
		fields = ('name', 'ABV', 'capacity', 'company', 'image')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		fields = ('name', 'ABV', 'capacity', 'company', 'image')

class MakgeolliSerializer(serializers.ModelSerializer):
	class Meta:
		model = Makgeolli
		fields = ('name', 'ABV', 'capacity', 'company', 'image')


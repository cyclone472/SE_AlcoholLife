from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)

class Drink(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ABV = models.FloatField()
	capacity = models.PositiveIntegerField()
	image = models.CharField(max_length=100, blank=True)
	company = models.CharField(max_length=100)
	rating = models.DecimalField(decimal_places=1, max_digits=2, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

'''
class Soju(models.Model):
	name = models.CharField(max_length=100)
	ABV = models.FloatField()
	capacity = models.PositiveIntegerField()
	company = models.CharField(max_length=100)
	image = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Beer(models.Model):
	name = models.CharField(max_length=100)
	ABV = models.FloatField()
	capacity = models.PositiveIntegerField()
	company = models.CharField(max_length=100)
	image = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Makgeolli(models.Model):
	name = models.CharField(max_length=100)
	ABV = models.FloatField()
	capacity = models.PositiveIntegerField()
	company = models.CharField(max_length=100)
	image = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
'''

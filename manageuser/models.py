from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from drink.models import * 

# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    comment_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Review, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

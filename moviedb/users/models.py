from django.db import models
from django.contrib.auth.models import User
from database.models import Rating

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorite_movie = models.CharField(max_length=50)
    ratings = models.ManyToManyField(Rating)

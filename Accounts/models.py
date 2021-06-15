from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    verified = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    followers_count = models.IntegerField
    follows_count = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.name = self.first_name + " " + self.last_name
        return self.name


class UserSocial(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



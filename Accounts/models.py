from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    verified = models.BooleanField(default=False)
    status = models.CharField(max_length=255)
    followers_count = models.IntegerField
    follows_count = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # self.name = self.first_name + " " + self.last_name
        return self.email


class UserSocial(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    token_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField
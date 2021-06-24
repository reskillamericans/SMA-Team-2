from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    class AccountStatus(models.TextChoices):
        LOCKED = 'Locked', 'Locked'
        UNLOCKED = 'Unlocked', 'Unlocked'

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    account_status = models.CharField(max_length=10, choices=AccountStatus.choices, default=AccountStatus.UNLOCKED)
    followers_count = models.IntegerField(default=0)
    follows_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # self.name = self.first_name + " " + self.last_name
        return self.email


class UserSocial(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=255, blank=True)
    instagram_link = models.CharField(max_length=255, blank=True)
    twitter_link = models.CharField(max_length=255, blank=True)
    linkedin_link = models.CharField(max_length=255, blank=True)
    github_link = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class User(AbstractUser):
    class AccountStatus(models.TextChoices):
        LOCKED = 'Locked', 'Locked'
        UNLOCKED = 'Unlocked', 'Unlocked'

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    occupation = models.CharField(max_length=255, null=True, blank=True, default=None)
    bio = models.TextField(null=True, blank=True, default=None)
    verified = models.BooleanField(default=False, null=True, blank=True)
    account_status = models.CharField(max_length=10, choices=AccountStatus.choices, default=AccountStatus.UNLOCKED, null=True, blank=True)
    followers_count = models.IntegerField(default=0, null=True, blank=True)
    follows_count = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email


class UserSocial(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    facebook_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    instagram_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    twitter_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    linkedin_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    github_link = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user_id.username


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    token = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
    token_used = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Password Resets"
        ordering = ['user_id']

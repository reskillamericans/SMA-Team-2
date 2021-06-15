from django.db import models
from django.conf import settings


# Create your models here.


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    token_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    receiver_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="message_receiver")
    sender_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="message_sender")
    content = models.TextField
    read_at = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following")
    follower_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL)
    content = models.TextField
    likes = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    id = models.AutoField(primary_key=True)
    commenter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostLike(models.Model):
    id = models.AutoField(primary_key=True)
    liker_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

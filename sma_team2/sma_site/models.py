from django.db import models
from datetime import datetime

# Create your models here.


class Users(models.Model):
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


class PasswordResets(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    token_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField


class Socials(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    receiver_id = models.ManyToManyField(Users, related_name="message_receiver")
    sender_id = models.ManyToManyField(Users, related_name="message_sender")
    content = models.TextField
    read_at = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Followers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(Users, related_name="following")
    follower_id = models.ManyToManyField(Users, related_name="follower")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(PostCategories, null=True, on_delete=models.SET_NULL)
    content = models.TextField
    likes = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComments(models.Model):
    id = models.AutoField(primary_key=True)
    commenter_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostLikes(models.Model):
    id = models.AutoField(primary_key=True)
    liker_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

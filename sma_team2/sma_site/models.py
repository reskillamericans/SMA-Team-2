from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
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


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    token_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField


class Social(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    receiver_id = models.ManyToManyField(User, related_name="message_receiver")
    sender_id = models.ManyToManyField(User, related_name="message_sender")
    content = models.TextField
    read_at = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(User, related_name="following")
    follower_id = models.ManyToManyField(User, related_name="follower")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL)
    content = models.TextField
    likes = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    id = models.AutoField(primary_key=True)
    commenter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostLike(models.Model):
    id = models.AutoField(primary_key=True)
    liker_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

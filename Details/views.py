from django.http import HttpResponse
from django.shortcuts import  redirect
from .models import Post

# Create your views here.


# Like/Unlike Post Feature
def like_post(request, post_id):

    if not request.user.is_authenticated:
        return redirect("index")

    post = Post.objects.get(id=post_id)

    is_liked_by_user = False

    # Check if logged in user has liked this post.
    for user_like in post.likes.all():
        if user_like == request.user:
            is_liked_by_user = True
            break

    if not is_liked_by_user:
        post.likes.add(request.user)

    return HttpResponse()


def unlike_post(request, post_id):

    if not request.user.is_authenticated:
        return redirect("index")

    post = Post.objects.get(id=post_id)

    is_liked_by_user = False

    # Check if logged in user has liked this post.
    for user_like in post.likes.all():
        if user_like == request.user:
            is_liked_by_user = True
            break

    if is_liked_by_user:
        post.likes.remove(request.user)

    return HttpResponse()

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from Accounts.models import User
from .models import Post, PostCategory, Message

# Create your views here.


def create_post(request):
    if not request.user.is_authenticated:
        return redirect("index")
    if request.method != 'POST':
        return render(request, "create_post.html")
    if not request.POST.get('title') and request.POST.get('content'):
        context = {'error': 'The post was not successfully created. Please enter a title and content'}
        return render(request, 'create_post.html', context)
    post = Post()
    post.user_id = request.user
    post_category_id = request.POST.get('category')
    post.post_category_id = get_category_id(post_category_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    messages.success(request, "Your post has been successfully created")
    return render(request, 'create_post.html')



def get_category_id(category):
    if category == '':
        return None
    # If category exists, return category
    try:
        post_category = PostCategory.objects.get(name=category)
        return post_category
    except PostCategory.DoesNotExist:
        # Else Create category
        new_category = PostCategory(name=category)
        new_category.save()
        return new_category


def delete_post(request, id):
    if not request.user.is_authenticated:
        return redirect("index")
    post = Post.objects.get(id=id)
    if request.user == post.user_id:
        Post.objects.get(id=id).delete()
    return redirect('index')


def update_post(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    try:
        post = get_object_or_404(Post, id=id)
    except Post.DoesNotExist:
        return redirect('index')

    if not request.user == post.user_id:
        return redirect('index')
    if request.method != 'POST':
        context = {'postobj': post,
                   'error': 'The post was not successfully updated. The title and content must be filled out.'}
        return render(request, "update_post.html", context)
    post.post_category_id = get_category_id(request.POST.get('category'))
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    messages.success(request, "The post was successfully updated")
    context = {'postobj': post}

    return render(request, 'update_post.html', context)


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


def send_message(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    try:
        receiver = get_object_or_404(User, id=id)
    except User.DoesNotExist:
        messages.error("User does not exist")
        return redirect("index")

    if request.method != 'POST':
        return render(request, "send_message.html")

    if not request.POST.get('messageobj'):
        context = {'error': 'The message was not successfully sent. Please enter content'}
        return render(request, 'send_message.html', context)
    message = Message()
    message.sender_id = request.user
    message.receiver_id = receiver
    message.content = request.POST.get('messageobj')
    message.save()
    messages.success(request, "Your message was successfully sent")
    return render(request, 'send_message.html')


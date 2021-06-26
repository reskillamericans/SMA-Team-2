from django.shortcuts import render, redirect

# Create your views here.

from .models import Post, PostCategory


def create_post(request):
    if not request.user.is_authenticated:
        return redirect("index")
    if request.method != 'POST':
        return render(request=request, template_name="create_post.html")
    if not request.POST.get('title') and request.POST.get('content'):
        return redirect("index")
    post = Post()
    post.user_id = request.user
    post.post_category_id = get_category_id(request.POST.get('category'))
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect("index")



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
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')

    if not request.user == post.user_id:
        return redirect('index')
    if request.method != 'POST':
        return render(request=request, template_name="update_post.html")
    post.post_category_id = get_category_id(request.POST.get('category'))
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('index')

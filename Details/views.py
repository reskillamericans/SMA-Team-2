from django.shortcuts import render, redirect

# Create your views here.

from .models import Post, PostCategory


def create_post(request):
    if not request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.user_id = request.user
            post_category_id = get_category_id(request.POST.get('category'))
            if post_category_id is not None:
                post.post_category_id = post_category_id
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            return render(request=request, template_name="create_post.html")
    else:
        return render(request=request, template_name="create_post.html")


def get_category_id(category):

    if category == '':
        return None
    # If category exists, return category
    try:
        post_category = PostCategory.objects.get(name=category)
        return post_category
    except PostCategory.DoesNotExist:
        # Else Create category
        category = PostCategory(name=category)
        category.save()
        return category


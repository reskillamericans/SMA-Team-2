from django.urls import path 

from. import views
from Accounts import views as accountViews

urlpatterns = [
    path('', accountViews.index, name='index'),
    path('like_post/<post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<post_id>/', views.unlike_post, name='unlike_post'),
]
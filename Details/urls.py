from django.urls import path 
from. import views

urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path("update_post/<int:id>/", views.update_post, name="update_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
    path('like_post/<post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<post_id>/', views.unlike_post, name='unlike_post'),
    path('send_message/<int:id>/', views.send_message, name='send_message', api_name="details"),
]




from django.urls import path 

from. import views

urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path("update_post/<int:id>/", views.update_post, name="update_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
]

from django.urls import path 

from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', views.password_reset_done_request, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm_request, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete_request, name='password_reset_complete'),
    path('post/<int:pk>/comment', views.post_comment_request, name='comment')
]

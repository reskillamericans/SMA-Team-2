from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(PasswordReset)
admin.site.register(UserSocial)
admin.site.register(Message)
admin.site.register(Follower)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)

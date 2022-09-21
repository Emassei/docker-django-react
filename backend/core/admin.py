from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User
from .models import Post


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

admin.site.register(Post)

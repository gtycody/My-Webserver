from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from userprofile.models import Profile

# Register your models here.

from .models import Post

admin.site.register(Post)


from django.contrib import admin


# Register your models here.

from .models import Post
from .models import Code
from .models import Photo

admin.site.register(Post)
admin.site.register(Code)
admin.site.register(Photo)


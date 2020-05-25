from django import forms
# 引入文章模型
from .models import Post
from .models import Code
from .models import Photo

# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','author')


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ('title', 'content','author')


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'content','author')
from django import forms
# 引入文章模型
from .models import Post

# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','author')


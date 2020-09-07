from django import forms
# 引入文章模型
from .models import Post
from .models import Photo

# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','post_type')

class PhotoPostForm(forms.ModelForm):
    Photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Photo
        fields = ('title','Photos')


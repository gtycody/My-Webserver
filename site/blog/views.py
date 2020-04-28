
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

def article_list(request):
    articles = Post.objects.all()
    context={'articles':articles}
    return render(request, 'list.html', context)

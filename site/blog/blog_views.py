from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
import markdown

def article_list(request):
    articles = Post.objects.all()
    context = {'articles': articles}
    return render(request, 'list.html', context)


def article_content(request,id):
    articles = Post.objects.get(id=id)
    articles.content = markdown.markdown(articles.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])
    context = {'article': articles}
    return render(request, 'page.html', context)








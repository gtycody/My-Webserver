from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from userprofile import user_views
import markdown

def article_list(request):
    articles = Post.objects.all()
    context = {'articles': articles}
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
    print(context)
    return render(request, 'list.html', context)


def article_content(request,id):
    articles = Post.objects.get(id=id)
    articles.content = markdown.markdown(articles.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])
    context = {'article': articles}
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
    return render(request, 'page.html', context)








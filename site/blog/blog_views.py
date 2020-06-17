from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from userprofile import user_views
import markdown
from .forms import ArticlePostForm

def article_list(request, types):
    articles = Post.objects.filter(post_type = types )
    context = {'articles': articles}
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
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


def article_create(request):

    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        print(article_post_form)
        print(request.session.get('user_id'))
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(request.session.get('user_id'))
            new_article.save()
            return redirect('homepage')
        else:
            return HttpResponse("invalid")
    else:
        article_post_form = ArticlePostForm()
        context = { 'article_post_form': article_post_form }
        avatar = request.session.get('avatar')
        context['avatar'] = avatar
        return render(request, 'write.html', context)




from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post,Photo
from userprofile import user_views
import markdown
from .forms import ArticlePostForm, PhotoPostForm
from datetime import datetime,timedelta

def article_list(request, types):

    articles = Post.objects.filter(post_type = types)

    for i in articles:
        i.created_on =i.created_on.date
        i.updated_on =i.updated_on.date

    context = {'articles': articles}
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
    print(context)

    if(types == 0):
        context['post_type']="Article"
        return render(request, 'article_list.html', context)
    elif(types == 1):
        context['post_type']="Project"
        return render(request, 'code_list.html', context)
    elif(types == 2):
        context['post_type']="Photo"
        return render(request, 'photo_list.html', context)

    


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
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id = int(request.session.get('user_id')))
            new_article.save()
            return redirect('homepage')
        else:
            return HttpResponse("invalid")
    else:
        article_post_form = ArticlePostForm()
        print(article_post_form)
        context = { 'article_post_form': article_post_form }
        avatar = request.session.get('avatar')
        context['avatar'] = avatar
        return render(request, 'write.html', context)


def photo_create(request):

    if request.method == "POST":
        photo_post_form = PhotoPostForm(request.POST, request.FILES)
        #print(photo_post_form)
        #print(photo_post_form.is_valid())
        if photo_post_form.is_valid():
            print(request.FILES.getlist('Photos'))
            instance = photo_post_form.save(commit=False)
            instance.title = request.POST['title']
            for img in request.FILES.getlist('Photos'):
                instance = Photo(image = img)
                print("instance", instance)
                instance.author = User.objects.get(id = int(request.session.get('user_id')))
                instance.save()
            return redirect('homepage')
        else:
            return HttpResponse("invalid")

    else:
        photo_post_form = PhotoPostForm()
        context = {'form':photo_post_form}
        avatar = request.session.get('avatar')
        context['avatar'] = avatar
        #print("form: ",photo_post_form)
        return render(request,'photoUpLoad.html',context)
        
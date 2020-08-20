from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from userprofile import user_views


def homepage(request):   
    context = {}
    context['time'] = datetime.datetime.now()
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
    return render(request, 'homepage.html', context)

def mypage(request):
    return render(request, 'mypage.html')

def mysetting(request):
    return render(request,'mysetting.html')

def aboutUs(request):
    context = {}
    avatar = request.session.get('avatar')
    context['avatar'] = avatar
    return render(request,'aboutUs.html', context)


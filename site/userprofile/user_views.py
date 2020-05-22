from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data=user_login_form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                request.session['avatar'] = get_user_pic(user.id)
                return redirect('homepage')
            else:
                return HttpResponse("wrong username or password")
        else:
            return HttpResponse("invalid login")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context ={'frorm':user_login_form}
        return render(request,'login.html',context)
    else:
        return HttpResponse("wrong request type")


def get_user_pic(id):
    profile = Profile.objects.get(user_id = id)
    return profile.avatar.url


def user_logout(request):
    logout(request)
    return redirect('homepage')


def profile_content(request,id):
    user = User.objects.get(id = id)
    user_profile = Profile.objects.get(user_id=id)
    context = {'user_profile': user_profile}
    return render(request, 'mypage.html', context)


def profile_edit(request, id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user_id=id)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("not authorized")
    
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.email= profile_cd['email']
            profile.save()

            return redirect("userprofile:edit",id = id)
        else:
            return HttpResponse("plz re-enter")
    
    elif request.method == "GET":
        profile_form = ProfileForm()
        context = {'profile_form' : profile_form, 'profile':profile, 'user':user}
        return render(request,'userprofile/mysetting.html',context)
    
    else:
        return HttpResponse("cant identify request")

    profile_form = ProfileForm(request.POST,request.FILES)

    if profile_form.is_valid():
        if 'avatar' in request.FILES:
            profile.avatar = profile_cd["avatar"]
            





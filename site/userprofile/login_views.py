from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data=user_login_form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
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

def user_logout(request):
    logout(request)
    return redirect('homepage')

def profile_edit(request, id):
    profile_form = ProfileForm(request.POST,request.FILES)

    if profile_form.is_valid():
        if 'avator' in request.FILES:
            profile.avator = profile_cd["avatar"]
            





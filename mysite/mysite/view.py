from django.http import HttpResponse
from django.shortcuts import render
import datetime

def homepage(request):
    context = {}
    context['hello'] = 'Welcome to My Blog'
    context['time'] = datetime.datetime.now()
    return render(request, 'hello.html', context)


from django.urls import path
from django.conf.urls import url
from . import view

urlpatterns = [
    path('homepage/', view.homepage),
]
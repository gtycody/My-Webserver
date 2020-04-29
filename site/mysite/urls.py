from django.urls import path
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from . import view
from blog import views

urlpatterns = [
    path('homepage/', view.homepage),
    path('article/', view.article),
    path('code/', view.code),
    path('admin/',admin.site.urls),
    path('articles/',views.article_list),
]
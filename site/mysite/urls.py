from django.urls import path
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .import views
from blog import blog_view

urlpatterns = [
    path('homepage/', views.homepage),
    path('article/', views.article),
    path('code/', views.code),
    path('blog/admin/',admin.site.urls),

    path('blog/',blog_view.article_list),
    path('blog/content/<int:id>/',blog_view.article_content),
]
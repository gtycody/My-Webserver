from django.urls import path
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .import views
from blog import blog_views
from userprofile import login_views

urlpatterns = [
    url(r'^homepage/',views.homepage,name='homepage'),
    url(r'^code/', views.code),
    url(r'^blog/admin/',admin.site.urls),

    path('blog/',blog_views.article_list,name='blog'),
    path('blog/<int:id>/',blog_views.article_content),
    path('login/',login_views.user_login,name='login'),
    path('logout/',login_views.user_logout, name='logout'),
]
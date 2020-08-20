from django.urls import path
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .import views
from blog import blog_views
from userprofile import user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^homepage/',views.homepage,name='homepage'),
    url(r'^admin/',admin.site.urls),
    
    url(r'^mypage/mysetting', views.mysetting, name='mysetting'),
    
    path('create_new_post/',blog_views.article_create, name = 'new_post'),

    path('mypage/<int:id>/',user_views.profile_content, name='mypage'),

    path('aboutUs/',views.aboutUs, name='aboutUs'),


    path('blog/<int:types>',blog_views.article_list,name='blog'),
    path('blog/content/<int:id>/',blog_views.article_content,name = 'blog_content'),


    path('login/',user_views.user_login,name='login'),
    path('logout/',user_views.user_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


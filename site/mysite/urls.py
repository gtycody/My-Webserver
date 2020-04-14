from django.urls import path
from django.conf.urls import url
from . import view
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('homepage/', view.homepage),
    path('article/', view.article),
    path('code/', view.code),
    url(r'^admin/', include(admin.site.urls))
]
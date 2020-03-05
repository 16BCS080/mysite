from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = [    
    url(r'^$',include('posts.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^posts/',include('posts.urls')),
]

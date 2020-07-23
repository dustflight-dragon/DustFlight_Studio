"""
Definition of urls for DustFlight_Studio.
"""

from datetime import datetime
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import serve

from Blog import views

# from Blog import calc

admin.autodiscover()

urlpatterns = [
    path(r'', views.hello, name='blog_hello'),
    path(r'hello', views.hello, name='blog_hello'),
    path(r'index', views.hello, name='blog_hello'),
    path(r'blog', views.index, name='blog_index'),
    path(r'blog/index', views.index, name='blog_index'),
    path(r'blog/about', views.about, name='blog_about'),
    path(r'blog/list_whole_article', views.list_whole_article,
         name='blog_list_whole_article'),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    # url(r'^blog/calc/(\d+)/(\d+)/$', calc.try_addition_compute,
    # name='try_addition_compute'),
    path(r'admin/', admin.site.urls), ]

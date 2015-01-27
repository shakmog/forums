from django.conf.urls import patterns, include, url
from django.contrib import admin
from forums.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='index'),
)

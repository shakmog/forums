from django.conf.urls import patterns, include, url
from django.contrib import admin
from forums.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^a_t_c', AdminThreadCreate.as_view(), name='a_t_c'),
    url(r'^a_t_d', AdminThreadDelete.as_view(), name='a_t_c'),
    url(r'^a_p_c', AdminPostCreate.as_view(), name='a_p_c'),
    url(r'^a_p_d', AdminPostDelete.as_view(), name='a_p_d'),
    url(r'^a_f_c', AdminForumCreate.as_view(), name='a_f_c'),
    url(r'^a_f_d', AdminForumDelete.as_view(), name='a_f_d'),
    url(r'^forums', ForumsView.as_view(), name='forums'),
    url(r'^threads/(?P<pk>\d+)', ThreadsView.as_view(), name='threads'),
    url(r'^posts/(?P<pk>\d+)', PostsView.as_view(), name='posts'),
    url(r'^signup', Signup.as_view(), name='signup'),
    url(r'^$', Login.as_view(), name='login'),
    url(r'^user_view', UserView.as_view(), name = 'user_view'),
)

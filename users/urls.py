from django.conf.urls import patterns, include, url
from users.views import *

urlpatterns = patterns('',
	url( r'^/all', AllView.as_view(), name = 'all' ),
    url( r'^/signup', Signup.as_view(), name = 'signup' ),
    url( r'^/admin/create', AdminSignup.as_view(), name = 'admin_signup' ),
    url( r'^/admin/login', AdminLogin.as_view(), name = 'admin_login' ),
    url( r'^logout', Logout.as_view(), name = 'logout' ),
    url( r'^/login', Login.as_view(), name = 'login' ),
)

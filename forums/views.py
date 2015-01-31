from django.shortcuts import render, redirect
from django.views.generic import View
from forums.models import *
from users.forms import *


# Create your views here.
class Login( View ):
	template_name = 'forums/login.html'
	form_class = AuthenticationForm

	def get( self, request ):
		request.context_dict['form'] = self.form_class
		return render( request, self.template_name, request.context_dict )


class Signup( View ):
	template_name = 'forums/signup.html'
	form_class = UserCreationForm

	def get( self, request ):
		request.context_dict['form'] = self.form_class
		return render( request, self.template_name, request.context_dict )

class UserView( View ):
	template_name = "forums/user_view.html"

	def get( self, request ):
		request.context_dict['users'] = User.objects.all()
		request.context_dict['counts'] = User.objects.count()
		return render( request, self.template_name, request.context_dict )

class ForumsView( View ):
	template_name = "forums/forums.html"

	def get( self, request ):
		forums = Forums.objects.all()
		threads_count = Threads.objects.count()
		posts_count = Post.objects.count()
		request.context_dict['forums'] = forums
		request.context_dict['threads_count'] = threads_count
		request.context_dict['posts_count'] = posts_count
		return render( request, self.template_name, request.context_dict )


class ThreadsView( View ):
	template_name = "forums/threads.html"

	def get( self, request ):
		threads = Threads.objects.all()
		request.context_dict['threads'] = threads
		return render( request, self.template_name, request.context_dict )


class PostsView( View ):
	template_name = "forums/posts.html"	

	def get( self, request ):
		posts = Posts.objects.all()
		request.context_dict['posts'] = posts
		return render( request, self.template_name, request.context_dict )

class AdminThreadCreate( View ):
	pass

class AdminThreadDelete( View ):
	pass

class AdminPostCreate( View ):
	pass

class AdminPostDelete( View ):
	pass

class AdminForumCreate( View ):
	pass

class AdminForumDelete( View ):
	pass
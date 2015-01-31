from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from users.forms import *

# Create your views here.

class AllView( View ):
	pass

class Login( View ):
	template_name = 'forums/login.html'
	form_class = AuthenticationForm

	def post( self, request ):
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		print('first')
		if user:
			print("login")
			login(request, user)
			return redirect( "/forums/" )
		else:
			print('not logeed in')
			request.context_dict['form'] = self.form_class
			request.context_dict['errors'] = "Wrong username/password combination."
			return render( request, self.template_name, request.context_dict)


class Signup( View ):
	template_name = "forums/signup.html"
	form_class = UserCreationForm

	def post( self, request ):
		form = self.form_class( request.POST )
		if form.is_valid():
			print('valid')
			user = form.save()
			user = authenticate(username=user, password=user.password)
			return redirect( "/forums/" )
		else:
			print('not')
			request.context_dict['form'] = self.form_class
			request.context_dict['errors'] = "NO GO."
			return render( request, self.template_name, request.context_dict)

class Logout( View ):
	pass

class AdminSignup( View ):
	template_name = "users/signup.html"
	form_class = AdminCreationForm

	def get( self, request ):
		request.context_dict['form'] = self.form_class
		return render( request, self.template_name, request.context_dict )


class AdminLogin( View ):
	template_name = "users/login.html"
	form_class = AuthenticationForm

	def get( self, request ):
		request.context_dict['form'] = self.form_class
		return render( request, self.template_name, request.context_dict )
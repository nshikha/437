from django.shortcuts import render, redirect
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from app.models import *

import datetime

# Create your views here.

@login_required
def profile(request):
	if (request.POST):
 		text = request.POST.get("text")
 		if (text):
			newPost = Post(text=text,user=request.user,publishedDate=datetime.date.today())
			newPost.save()

	posts = Post.objects.filter(user=request.user)
	keyword = request.GET.get("keyword")
	if (keyword):
		posts = posts.filter(text__icontains=keyword)
	return render(request, 'profile.html', {'posts' : posts, 'user':request.user})


@login_required
def feed(request):
	posts = Post.objects.exclude(user=request.user)
	keyword = request.GET.get("keyword")
	if (keyword):
		posts = posts.filter(text__icontains=keyword)

	return render(request, 'feed.html', {'posts': posts})

@login_required
def editProfile(request):
	errors = []

	if (request.POST):
		newName = request.POST.get('newName')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		newPassword = request.POST.get('newPassword')
		if (password1 or password2):
			if (password1 != password2):
				errors.append('Passwords did not match.')
			if (not newPassword):
				errors.append('Enter new password')

		if (errors):
			return render(request, 'editprofile.html', {'errors':errors, 'user':request.user})

		user = request.user
		if (newName and newName != user.username):
			user.username = newName
		if (newPassword and newPassword != user.password):
			user.set_password(newPassword)
		user.save()

		return redirect('/profile')

	return render(request, 'editprofile.html', {'errors':errors, 'user':request.user})




def register(request):
    context = {}
    errors = []
    context['errors'] = errors
    context['username'] = ""
    context['email'] = ""
    # Just display the registration form if this is a GET request
    if (request.method == 'GET'):
      return render(request, 'register.html', context)

    # Checks the validity of the form data
    if (not 'username' in request.POST or not request.POST['username']):
		  errors.append('Username is required.')
    else:
		  context['username'] = request.POST['username']

    if (not 'email' in request.POST or not request.POST['email']):
      errors.append('Email is required.')
    else:
      context['email'] = request.POST['email']

    if (not 'password1' in request.POST or not request.POST['password1']):
		  errors.append('Password is required.')
    if (not 'password2' in request.POST or not request.POST['password2']):
		  errors.append('Please Confirm password.')

    if ('password1' in request.POST and 'password2' in request.POST 
       and request.POST['password1'] and request.POST['password2'] 
       and request.POST['password1'] != request.POST['password2']):
		  errors.append('Passwords did not match.')

    if (len(User.objects.filter(username=request.POST['username'])) > 0):
		  errors.append('Username is already taken.')

    if errors:
      return render(request, 'register.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password1'],
                                        email=request.POST['email'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(request, new_user)
    return redirect('/profile')







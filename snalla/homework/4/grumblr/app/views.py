from django.shortcuts import render, redirect
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from app.models import *
from app.forms import *

import datetime

# Create your views here.

@login_required
def comment(request, post_id):
    path = request.path
    basePath = path.rsplit("/", 1)[0]
    text = request.POST.get("comment")
    post = get_object_or_404(Post, pk=post_id)
    if (text):
        grumbler = Grumbler.objects.get(user=request.user)
        newComment = Comment(text=text,author=grumbler, post=post)
        newComment.save()
    return redirect(basePath)

@login_required
def users(request):
    context = {'users': User.objects.all() }
    return render(request, 'tabs/users.html', context)

@login_required
def dislike(request, post_id):
    print "hi"
    path = request.path
    basePath = path.rsplit("/", 2)[0]
    print basePath
    ugrumbler = Grumbler.objects.get(user=request.user)
    post = Post.objects.get(pk=post_id)
    post.dislikes.add(ugrumbler)
    post.save()
    #user = User.objects.get(pk=user_id)
    #grumbler = Grumbler.objects.get(user=user)
    posts = Post.objects.filter(author=grumbler).order_by("-published_date")
    return render(request, 'tabs/profile.html', {'posts' : posts, 'grumbler':ugrumbler, 'ugrumbler':ugrumbler})
    #return redirect(basePath)

@login_required
def userprofile(request):
    if (request.POST):
        text = request.POST.get("text")
        if (text):
            grumbler = Grumbler.objects.get(user=request.user)
            newPost = Post(text=text,author=grumbler)
            newPost.save()
    return redirect('/profile/' + str(request.user.id))

@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    grumbler = Grumbler.objects.get(user=user)
    posts = Post.objects.filter(author=grumbler).order_by("-published_date")
    ugrumbler = Grumbler.objects.get(user=request.user)
    return render(request, 'tabs/profile.html', {'posts' : posts, 'grumbler':grumbler, 'ugrumbler':ugrumbler})


@login_required
def feed(request):
    ugrumbler = Grumbler.objects.get(user=request.user)
    posts = Post.objects.filter(author__in=ugrumbler.following.all()).exclude(author=ugrumbler).order_by("-published_date")
    showPosts = set([])
    for post in posts:
        if (ugrumbler not in post.author.blockers.all()):
            showPosts.add(post)
    return render(request, 'tabs/feed.html', {'posts': showPosts, 'ugrumbler':ugrumbler})

@login_required
def search(request):
    ugrumbler = Grumbler.objects.get(user=request.user)
    keyword = request.GET.get("keyword")
    posts = Post.objects.filter(text__icontains=keyword).order_by("-published_date")
    showPosts = set([])
    for post in posts:
        if (ugrumbler not in post.author.blockers.all()):
            showPosts.add(post)
    return render(request, 'tabs/feed.html', {'posts': posts, 'ugrumbler':ugrumbler})

@login_required
def follow(request, user_id):
    user = User.objects.get(pk=user_id)
    grumbler = Grumbler.objects.get(user=user)
    ugrumbler = Grumbler.objects.get(user=request.user)
    if (ugrumbler in grumbler.followers.all()):
        print "removing"
        grumbler.followers.remove(ugrumbler)
        ugrumbler.following.remove(grumbler)
    else:
        print "adding"
        grumbler.followers.add(ugrumbler)
        ugrumbler.following.add(grumbler)
    grumbler.save()
    ugrumbler.save()
    return redirect('/profile/' + str(user_id))


@login_required
def block(request, user_id):
    user = User.objects.get(pk=user_id)
    grumbler = Grumbler.objects.get(user=user)
    ugrumbler = Grumbler.objects.get(user=request.user)
    if (grumbler in ugrumbler.blockers.all()):
        ugrumbler.blockers.remove(grumbler)
    else:
        ugrumbler.blockers.add(grumbler)
    ugrumbler.save()
    return redirect('/profile/' + str(user_id))

@login_required
def editProfile(request):
    ugrumbler = Grumbler.objects.get(user=request.user)
    if (request.method == 'GET'):
        context = {'form' : EditProfileForm(), 'grumbler':ugrumbler}
        return render(request, 'tabs/editprofile.html', context)

    form = EditProfileForm(request.POST, request.FILES)
    if not form.is_valid():
        context = {'form' : form, 'grumbler':ugrumbler}
        return render(request, 'tabs/editprofile.html', context)
    user = request.user
    grumbler = Grumbler.objects.get(user=request.user)
    new_username = form.cleaned_data['username']
    new_password = form.cleaned_data['new_password']
    new_image = form.cleaned_data['image']
    if (new_username):
    	user.username = new_username
    if (new_password):
    	user.set_password(new_password)
    if (new_image):
        grumbler.image = new_image
        grumbler.save()
    user.save()
    return redirect('/profile')


def register(request):
    # Just display the registration form if this is a GET request
    if (request.method == 'GET'):
    	context = {'form' : RegisterForm()}
    	return render(request, 'login/register.html', context)

    # Creates the new user from the valid form data
    # populates form with data automatically 
    form = RegisterForm(request.POST)
    if not form.is_valid():
    	context = {'form' : form}
    	return render(request, 'login/register.html', context)

    #question: do we do form.save()?
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'])
    new_user.save()
    new_grumbler = Grumbler.objects.create(user=new_user)
    new_grumbler.save()

    # Logs in the new user and redirects to his/her todo list
    user = authenticate(username=request.POST['username'], \
                        password=request.POST['password'])
    login(request, user)
    return redirect('/profile')







from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like

def bloglike(request, pid):
	post = get_object_or_404(Post, idcode=pid)
	author = Coder.objects.get(user = request.user)
	try:
		like = Like.objects.get(post=post, author=author)
		like.delete()
	except Like.DoesNotExist:
		like = Like(post=post, author=author)
		like.save()
	return redirect('/blogs/blogs/{}'.format(pid))
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.blog.blog import Post

def viewblogs(request):
	all_blogs = Post.objects.all()
	return render(request,"blog.html",{"all_blogs":all_blogs})
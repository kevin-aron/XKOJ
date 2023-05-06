from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import BlogsForm
from django.forms import inlineformset_factory
from machine.models.coder.coder import Coder
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like
from machine.models.blog.category import Category
from machine.models.blog.tags import Tags

def addblog(request):
	if not request.user.is_authenticated:
		return redirect("/settings/login/")
	else:
		if request.method == 'POST':
			blog_form = BlogsForm(request.POST)
			if blog_form.is_valid():
				blog = blog_form.save(commit=False)
				author = Coder.objects.get(user = request.user)
				blog.writer = author
				blog.save()
				return redirect("/blogs/blogs/")
			else:
				return redirect("/blogs/addblog/")
		else:
			blog_form = BlogsForm()
			
			return render(request, "blogs/addblog.html", {"blog_form":blog_form})
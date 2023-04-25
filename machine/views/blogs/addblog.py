from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import BlogsForm
from machine.models.blog.blog import Post

def addblog(request):
	if not request.user.is_authenticated:
		return redirect("/settings/login/")
	else:
		if request.method == 'POST':
			blog_form = BlogsForm(request.POST, request.FILES)
			if blog_form.is_valid():
				blog = blog_form.save()
				blog.writer = request.user.username
				blog.link = "/blogs/blogs/%" % (blog.idcode)
				blog.save()
			return redirect("/blogs/blogs/")
		else:
			blog_form = BlogsForm()
			return render(request, "blogs/addblog.html", {"blog_form":blog_form})
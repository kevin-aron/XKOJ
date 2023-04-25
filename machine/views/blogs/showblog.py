from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.blog.blog import Post
from machine.forms import CommentForm

def showblog(request, pid):
	post = get_object_or_404(Post, idcode=pid)
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
		return redirect('/blogs/blogs/{}'.format(post.idcode))
	else:
		comment_form = CommentForm()
	context = {'post': post, 'comment_form': comment_form}
	return render(request, 'blogs/showblog.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like
from machine.forms import CommentForm

def showblog(request, pid):
	post = get_object_or_404(Post, idcode=pid)
	comments = Comment.objects.filter(post=post)
	like = Like.objects.filter(post=post)
	likenum = 0
	for i in like:
		likenum += 1
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
	
	return render(request, 'blogs/showblog.html', {'post': post, 'comments':comments, 'likenum':likenum, 'comment_form': comment_form})
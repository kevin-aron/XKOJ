from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like
from machine.forms import CommentForm
import markdown
from markdown.extensions.toc import TocExtension
import re
from django.utils.text import slugify

def showblog(request, pid):
	post = get_object_or_404(Post, idcode=pid)
	comments = Comment.objects.filter(post=post)
	like = Like.objects.filter(post=post)
	coder = Coder.objects.get(user = request.user)
	image_path = str(coder.avatar)
	image_path = image_path[7:]
	likenum = 0
	for i in like:
		likenum += 1
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.post = post
			author = Coder.objects.get(user = request.user)
			comment.author = author
			comment.save()
		return redirect('/blogs/blogs/{}'.format(post.idcode))
	else:
		comment_form = CommentForm()
	#
	md = markdown.Markdown(extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.fenced_code',
		'markdown.extensions.toc',
		TocExtension(slugify=slugify),
	])
	post.content = md.convert(post.content)
	m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
	post.toc = m.group(1) if m is not None else ''
	
	return render(request, 'blogs/showblog.html', {'pid':pid, 'post': post, 'comments':comments, 'likenum':likenum, 'comment_form': comment_form,'image_path':image_path})
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import markdown
from markdown.extensions.toc import TocExtension
import re
from django.utils.text import slugify

def about(request):
	with open('about.md') as f:
		tnight = f.read()
		f.close()
	md = markdown.Markdown(extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.fenced_code',
		'markdown.extensions.toc',
		TocExtension(slugify=slugify),
	])
	tnight = md.convert(tnight)
	return render(request,"blogs/about.html",{"tnight":tnight})
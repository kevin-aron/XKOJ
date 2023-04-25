from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import markdown

def about(request):
	with open('about.md') as f:
		tnight = f.read()
		f.close()
	print(markdown.markdown(tnight,extensions=['markdown.extensions.toc']))
	return render(request,"blogs/about.html",{"tnight":tnight})
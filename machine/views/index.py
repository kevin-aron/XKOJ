from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import markdown
from django.conf import settings

def index(request):
	with open('announcement.md') as f:
		announcement = f.read()
		f.close()
	print(markdown.markdown(announcement,extensions=settings.MARKDOWN_EXTENSIONS))
	return render(request, "settings/announcement.html", {"announcement":announcement})
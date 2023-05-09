from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
import requests
from bs4 import BeautifulSoup
def crabug(request):
	if request.method == 'POST':
		url = request.POST.get('url')
		response = requests.get(url)
		soup = BeautifulSoup(response.content, 'html.parser')
		content = soup.get_text()
		return render(request, 'problems/crabug.html', {'content': content})
	else:
		return render(request, 'problems/crabug.html')
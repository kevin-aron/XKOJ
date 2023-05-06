from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder

def message(request):
	coder = Coder.objects.get(user = request.user)
	image_path = str(coder.avatar)
	image_path = image_path[7:]
	return render(request, 'settings/message.html', {"coder":coder,"image_path":image_path})
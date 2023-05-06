from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder


def register(request):
	registered = False
	if request.method == 'POST':
		avatar = request.FILES.get('avatar')
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			u_now = user_form.save()
			u_now.set_password(u_now.password)
			u_now.save()
			coder = Coder(user = u_now)
			if avatar:
				coder.avatar = avatar
			coder.link = '/users/%s' % (u_now.username)
			coder.rating = 900
			coder.trynum = 0
			coder.acnum = 0
			coder.blognum = 0
			coder.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	
	return render(request,'settings/register.html',{"user_form":user_form,"registered":registered})
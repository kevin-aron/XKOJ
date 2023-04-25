from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem

def allproblems(request):
	all_problems = Problem.objects.all()
	return render(request,"problems/problems.html",{"all_problems":all_problems})
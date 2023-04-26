from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
import markdown
from django.conf import settings

def viewproblem(request,pid):
	problem = get_object_or_404(Problem, code=pid)
	return render(request, "problems/oneproblem.html", {"problem":problem})
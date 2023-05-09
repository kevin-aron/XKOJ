from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.game.game import Game
from datetime import datetime

def games(request):
	try:
		games = Game.objects.all().order_by('-timestart')
		return render(request, 'games/game.html', {'games':games})
	except:
		return render(request, 'games/game.html')

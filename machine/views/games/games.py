from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.game.game import Game

def games(request):
	gamesnotstart = Game.objects.filter(status=0).order_by('-timestart')
#	gameing = Game.objects.filter(status=1).order_by('-timestart')
#	gamesend = Game.objects.filter(status=2).order_by('-timestart')
	return render(request, 'games/game.html', {"gamesnotstart":gamesnotstart})
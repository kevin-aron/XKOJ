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
	now = datetime.now()
	flag_notstart = 0
	flag_ing = 0
	flag_end = 0
	try:
		gamesnotstart_temp = Game.objects.filter(status=0).order_by('-timestart')
		for g in gamesnotstart_temp:
			if g.timeend < now:
				g.status = 2
				g.save()
			elif g.timeend > now and g.timestart <= now:
				g.status = 1
				g.save()
		try:
			gamesnotstart = Game.objects.filter(status=0).order_by('-timestart')
			flag_notstart = 1
		except:
			pass
	except:
		pass
	try:
		gameing_temp = Game.objects.filter(status=1).order_by('-timestart')
		for g in gameing_temp:
			if g.timeend < now:
				g.status = 2
				g.save()
		try:
			gameing = Game.objects.filter(status=1).order_by('-timestart')
			flag_ing = 1
		except:
			pass
	except:
		pass
	try:
		gamesend = Game.objects.filter(status=2).order_by('-timestart')
		flag_end = 1
	except:
		pass
	if flag_notstart and flag_ing and flag_end:
		return render(request, 'games/game.html', {"gamesnotstart":gamesnotstart,'gameing':gameing,'gamesend':gamesend})
	elif flag_notstart and flag_ing:
		return render(request, 'games/game.html', {"gamesnotstart":gamesnotstart,'gameing':gameing})
	elif flag_ing and flag_end:
		return render(request, 'games/game.html', {'gameing':gameing,'gamesend':gamesend})
	elif flag_notstart and flag_end:
		return render(request, 'games/game.html', {"gamesnotstart":gamesnotstart,'gamesend':gamesend})
	elif flag_notstart:
		return render(request, 'games/game.html', {"gamesnotstart":gamesnotstart})
	elif flag_ing:
		return render(request, 'games/game.html', {'gameing':gameing})
	elif flag_end:
		return render(request, 'games/game.html', {'gamesend':gamesend})
	else:
		return render(request, 'games/game.html')

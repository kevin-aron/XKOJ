from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.game.game import Game
from machine.models.game.gameproblem import GameProblem
from machine.models.game.gamesubmission import GameSubmission
from machine.models.game.gamerk import GameRk

def ingame(request,pid):
	registered = False
	if request.method == 'POST':
		coder = Coder.objects.get(user = request.user)
		flag = GameRk.objects.filter(player=coder).exists()
		if flag:
			return render(request, 'games/ingame.html')
		else:
			game = get_object_or_404(Game,code=pid)
			gamerk = GameRk(game=game, player=coder)
			gamerk.save()
			registered = True
			return render(request, 'games/enrollgame.html', {"registered":registered})
	else:
		return render(request, 'games/enrollgame.html')
	
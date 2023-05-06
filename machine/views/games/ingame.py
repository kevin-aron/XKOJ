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
	game = get_object_or_404(Game,code=pid)
	problems = GameProblem.objects.filter(game=game)
	gamerk = GameRk.objects.filter(game=game)
	gamesubmissions = GameSubmission.objects.filter(game=game)
	prodata = {}
	for p in problems:
		now_problem = p.problem
		problemcode = now_problem.code
		if problemcode not in prodata:
			prodata[problemcode] = { 'acnum':0 }
		cnt = 0
		for g in gamerk:
			now_user = g.player
			username = now_user.user.username	
			for s in gamesubmissions:
				if s.submitter == now_user and now_problem == s.problem and s.result == 'AC':
					cnt += 1
					break
		prodata[problemcode]['acnum'] = cnt
	
	if request.method == 'POST':
		coder = Coder.objects.get(user = request.user)
		flag = GameRk.objects.filter(player=coder).exists()
		if flag:
			return render(request, 'games/ingame.html', {"game":game, "problems":problems, "prodata":prodata})
		else:
			game.gamenum += 1
			game.save()
			gamerk = GameRk(game=game, player=coder)
			gamerk.save()
			registered = True
			return render(request, 'games/enrollgame.html', {"registered":registered})
	else:
		return render(request, 'games/enrollgame.html', {"game":game, "problems":problems, "prodata":prodata})
	
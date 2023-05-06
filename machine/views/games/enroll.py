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
from django.utils import timezone

def enroll(request,pid):
	game = get_object_or_404(Game,code=pid)
	problems = GameProblem.objects.filter(game=game)
	submissions = GameSubmission.objects.filter(game=game)
	now = timezone.now()
	if game.status == 0 or game.timeend < now:
		return render(request, 'games/enrollgame.html', {"game":game})
	if game.timestart > now:
		return render(request, 'games/enrollgame.html', {"game":game})
	if game.timestart <= now <= game.timeend:
		return render(request, 'games/enrollgame.html', {"game":game, "problems":problems, "submissions":submissions})
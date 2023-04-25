from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.game.game import Game
from django.utils import timezone

def enroll(request, gameid):
	game = get_object_or_404(Game,id=gameid)
	problems = Problem.objects.filter(game=game).order_by('id')
	submissions = GameSubmission.objects.filter(game=game, user=request.user)
	now = timezone.now()
	if game.status == 0 or game.timeend < now:
		return render(request, 'enrollgame.html', {"game":game, "problems":problems})
	if game.timestart > now:
		return HttpResponse('比赛还未开始')
	if game.timestart <= now <= timeend:
		return render(request, 'ingame.html', {"game":game, "problems":problems, "submissions":submissions})
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.game.game import Game
from machine.models.game.gameproblem import GameProblem
from machine.models.game.gamesubmission import GameSubmission
from machine.models.game.gamerk import GameRk

def ingamerk(request,pid):
	game = get_object_or_404(Game,code=pid)
	gamerk = GameRk.objects.filter(game=game).order_by('-totalac', 'failtime')
	problems = GameProblem.objects.filter(game=game).order_by('addnum')
	submissions = GameSubmission.objects.filter(game=game)
	return render(request, 'games/ingamerk.html', {"gamerk":gamerk, "problems":problems, "submissions":submissions,"gid":pid})
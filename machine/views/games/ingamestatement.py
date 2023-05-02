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

def ingamestatement(request,pid):
	game = get_object_or_404(Game,code=pid)
	submissions = GameSubmission.objects.filter(game=game).order_by('-subtime')
	return render(request, 'games/ingamestatement.html', {"gid":pid,"submissions":submissions})
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
	gamerk = GameRk.objects.filter(game=game)
	problems = GameProblem.objects.filter(game=game)
	gamesubmissions = GameSubmission.objects.filter(game=game)
	starttime = game.timestart
	endtime = game.timeend
	data = {}
	for g in gamerk:
		now_user = g.player
		username = now_user.user.username
		if now_user.user.username not in data:
			data[username] = {}
		for p in problems:
			now_problem = p.problem
			problemcode = now_problem.code
			for s in gamesubmissions:
				if s.subtime > endtime:
					continue
				if s.submitter == now_user and now_problem == s.problem:
					if problemcode not in data[username]:
						if s.result == 'AC':
							data[username][problemcode] = {'passtime':s.subtime, 'failtime':s.num_wa, 'actime':0, 'boolac':1}
						else:
							data[username][problemcode] = {'passtime':s.subtime, 'failtime':s.num_wa, 'actime':-1, 'boolac':0}
					else:
						if s.subtime < data[username][problemcode]['passtime'] and s.result == 'AC':
							data[username][problemcode]['passtime'] = s.subtime
							data[username][problemcode]['failtime'] = s.num_wa
							data[username][problemcode]['boolac'] = 1

	#
	for g in gamerk:
		now_user = g.player
		username = now_user.user.username
		if username not in data:
			continue
		alltime = 0
		failtime = 0
		totalac = 0
		for p in problems:
			now_problem = p.problem
			problemcode = now_problem.code
			if problemcode not in data[username]:
				continue
			if data[username][problemcode]['boolac'] == 0:
				continue
			totalac += 1
			onetime = data[username][problemcode]['passtime']- starttime
			minutime = int(onetime.total_seconds() // 60)
			data[username][problemcode]['actime'] = minutime
			failtime += data[username][problemcode]['failtime']
			alltime += minutime
			alltime += data[username][problemcode]['failtime']*20
			minutime = 0
		g.totalac = totalac
		g.failtime = failtime
		g.alltime = alltime
		g.save()

	gamerkk = GameRk.objects.filter(game=game).order_by('-totalac', 'failtime')
	newdata = {}
	for g in gamerkk:
		username = g.player.user.username
		newdata[username] = {}
		for p in problems:
			problemcode = p.problem.code
			newdata[username][problemcode] = {'passtime':-1, 'failtime':0, 'actime':-1, 'boolac':-1}
			if problemcode not in data[username]:
				continue
			else:
				newdata[username][problemcode] = data[username][problemcode]
				
	return render(request, 'games/ingamerk.html', {"gamerk":gamerkk, "problems":problems, "newdata":newdata, "gid":pid})

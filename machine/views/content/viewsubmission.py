from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from machine.forms import UserForm
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.submission import Submission
from machine.models.game.gamesubmission import GameSubmission

def viewsubmission(request, submission_id):
	gid = request.GET.get('gid')
	if gid != 'nogame':
		required_gamesub = get_object_or_404(GameSubmission, idnum=int(submission_id))
		if not required_gamesub.private or (required_gamesub.private and required_gamesub.submitter.user.username == request.user.username):
			return render(request, "games/gamesubmission.html", {"submission":required_gamesub})
		else:
			return redirect('/')
	else:
		required_sub = get_object_or_404(Submission, id=int(submission_id))
		if not required_sub.private or (required_sub.private and required_sub.submitter.user.username == request.user.username):
			return render(request, "submissions/submission.html", {"submission":required_sub})
		else:
			return redirect('/')
	
	
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.forms import UserForm, ProblemForm, SubmissionForm
from machine.tasks import evaluate_submission
import re
from django.utils.text import slugify
#from markdown.extensions.toc import TocExtension

def submitcode(request,pid):
	if not request.user.is_authenticated:
		return redirect('/settings/login/')
	else:
		if request.method == 'POST':
			sub_form = SubmissionForm(request.POST)
			if sub_form.is_valid():
				sub = sub_form.save()
				sub.problem = Problem.objects.get(code = pid)
				sub.submitter = Coder.objects.get(user = request.user)
				sub.save()
				evaluate_submission.delay(sub.id)
			else:
				payload = {"sub_form":sub_form, "pid":pid}
				return render(request, "submit.html", payload)
			return redirect('/content/submission/{}'.format(sub.id))
		else:
			sub_form = SubmissionForm()
			payload = {"sub_form":sub_form, "pid":pid}
			return render(request, "submit.html", payload)

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.forms import UserForm, ProblemForm, SubmissionForm
#from machine.tasks import evaluate_submission
import re
from django.utils.text import slugify
#from markdown.extensions.toc import TocExtension

def submitcode(request,pid):
	if not request.user.is_authenticated:
		return redirect('/settings/login/')
	else:
		return render(request, "submit.html")
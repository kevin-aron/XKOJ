from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.models.game.game import Game
from machine.models.game.gamesubmission import GameSubmission
from machine.forms import UserForm, ProblemForm, SubmissionForm
from machine.tasks import evaluate_submission, game_submission
import re
from django.utils.text import slugify

def submitcode(request,pid):
	if not request.user.is_authenticated:
		return redirect('/settings/login/')
	else:
		gid = request.GET.get('gid')
		if request.method == 'POST':
			sub_form = SubmissionForm(request.POST)
			if sub_form.is_valid():
				sub = sub_form.save()
				sub.problem = Problem.objects.get(code = pid)
				sub.submitter = Coder.objects.get(user = request.user)
				sub.save()
				if gid != 'nogame':
					game = get_object_or_404(Game,code=gid)	#我们将 Submission 对象的数据复制到 submission_data 字典中，并将其作为关键字参数传递给 GameSubmission 的构造函数。这样做的好处是，在调用 game_submission.delay() 方法之前，我们已经将需要传递的数据提取出来，并将其作为参数传递给异步任务。这样即使在任务执行期间发生了更改，我们也可以确保在任务中读取到正确的数据。
					submission_data = {
						'idcode':"{}_{}".format(sub.submitter,sub.id),
						'code':sub.code,
						'lang':sub.lang,
						'idnum':sub.id,
					}
					gamesubmission = GameSubmission(
						game = game, 
						problem = sub.problem,
						submitter = sub.submitter,
						**submission_data
					)
					gamesubmission.save()
					game_submission.delay(gid, gamesubmission.id, submission_data)
					sub.delete()
					return redirect('/content/submission/{}'.format(gamesubmission.id))
				else:
					evaluate_submission.delay(sub.id)
					return redirect('/content/submission/{}'.format(sub.id))
			else:
				payload = {"sub_form":sub_form, "pid":pid}
				return render(request, "submissions/submit.html", payload)
		else:
			sub_form = SubmissionForm()
			payload = {"sub_form":sub_form, "pid":pid, "gid":gid}
			return render(request, "submissions/submit.html", payload)

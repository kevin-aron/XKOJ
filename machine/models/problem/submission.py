from django.db import models
from django.utils import timezone
from django.urls import reverse
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase

class Submission(models.Model):
	LANGUAGES = (
				  ("C","GNU C"),
				  ("CPP","GNU C++"),
			  )
	STATUSES=(
				("NT", "Not tested"),
				("CE", "Compile Error"),
				("TL", "Time Limit Error"),
				("RE", "Runtime Error"),
				("AC", "Accepted"),
				("WA", "Wrong Answer"),
			)
	submitter = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem, default=None, null=True,on_delete=models.CASCADE)
	status = models.CharField(max_length=2, default="NT", choices=STATUSES)
	lang = models.CharField(max_length=4, default="CPP", choices=LANGUAGES)
	code = models.TextField(default="")
	created = models.DateTimeField(auto_now_add=True)
	private = models.BooleanField(default = True)
	ac_num = models.IntegerField(default=0)
	
	class Meta:
		verbose_name = '提交结果'
		verbose_name_plural = verbose_name
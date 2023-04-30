from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from machine.models.game.game import Game
from machine.models.problem.problem import Problem
from machine.models.coder.coder import Coder

class GameSubmission(models.Model):
	LANGUAGES = (
				  ("C","GNU C"),
				  ("CPP","GNU C++"),
				  ("JAVA","JAVAC"),
				  ("PYTHON3","PYTH3"),
			  )
	STATUSES=(
				("NT", "Not tested"),
				("CE", "Compile Error"),
				("TLE", "Time Limit Error"),
				("RE", "Runtime Error"),
				("AC", "Accepted"),
				("WA", "Wrong Answer"),
			)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	submitter = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem, null=True, on_delete=models.CASCADE)
	code = models.TextField()
	result = models.CharField(max_length=3, default="NT", choices=STATUSES)
	lang = models.CharField(max_length=10, default="CPP", choices=LANGUAGES)
	num_wa = models.IntegerField(default=0)
	num_ac = models.IntegerField(default=0)
	nowtime = models.IntegerField(default=0)
	subtime = models.DateTimeField(auto_now_add=True)
	idcode = models.CharField(max_length=100,unique=True,default='xxx')
	link = models.URLField(default=-1)
	idnum = models.IntegerField(default=1)

	class Meta:
		verbose_name = '比赛提交状态'
		verbose_name_plural = verbose_name
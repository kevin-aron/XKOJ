from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from machine.models.game.game import Game
from machine.models.problem.problem import Problem
from machine.models.coder.coder import Coder

class GameSubmission(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	submitter = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem, null=True, on_delete=models.CASCADE)
	code = models.TextField()
	result = models.CharField(max_length=20)
	num_wa = models.IntegerField(default=0)
	num_ac = models.IntegerField(default=0)
	subtime = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '比赛提交状态'
		verbose_name_plural = verbose_name
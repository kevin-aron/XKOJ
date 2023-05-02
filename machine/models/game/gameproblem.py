from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from machine.models.game.game import Game
from machine.models.problem.problem import Problem

class GameProblem(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem, null=True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = '比赛题目对应表'
		verbose_name_plural = verbose_name
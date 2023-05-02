from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from machine.models.game.game import Game
from machine.models.problem.problem import Problem
from machine.models.coder.coder import Coder

class GameCoder(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	coder = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = '比赛用户对应表'
		verbose_name_plural = verbose_name
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from machine.models.game.game import Game
from machine.models.problem.problem import Problem
from machine.models.coder.coder import Coder
from machine.models.game.gamesubmission import GameSubmission

class GameRk(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	playersubs = models.ForeignKey(GameSubmission, null=True, on_delete=models.CASCADE)
	totalac = models.IntegerField(default=0)
	failtime = models.IntegerField(default=0)

	class Meta:
		verbose_name = '比赛排名信息'
		verbose_name_plural = verbose_name
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Game(models.Model):
	gamename = models.CharField(max_length=100)
	code = models.CharField(max_length=20,unique=True)
	link = models.URLField(max_length=256,blank=True)
	timestart = models.DateTimeField(default=timezone.now)
	timeend = models.DateTimeField(default=timezone.now)
	status = models.IntegerField(default=0) # 0:未开始 1:进行中 2:已结束
	gamestatement = models.TextField(default=0)
	gamehard = models.IntegerField(default=0)
	gamenum = models.IntegerField(default=0)

	class Meta:
		verbose_name = '比赛信息'
		verbose_name_plural = verbose_name
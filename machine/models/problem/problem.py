from django.db import models
from django.utils import timezone
from django.urls import reverse

class Problem(models.Model):
	name = models.CharField('问题标题',max_length=255)
	code = models.CharField('问题路径',max_length=20,unique=True)
	link = models.URLField('问题链接')
	statement = models.TextField('问题描述')

	num_submissions = models.IntegerField(default=0)
	num_ac = models.IntegerField(default=0)
	num_wa = models.IntegerField(default=0)
	num_re = models.IntegerField(default=0)
	num_tle = models.IntegerField(default=0)
	num_ce = models.IntegerField(default=0)
	data_added = models.DateTimeField(auto_now_add=True)
	time_limit = models.IntegerField(default=1)
	score = models.IntegerField(default=1)
	source = models.CharField(max_length=255)
	num_tests=models.IntegerField(default=1)

	class Meta:
		verbose_name = '问题集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.code)
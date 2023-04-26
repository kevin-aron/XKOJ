from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Coder(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.URLField(max_length=256,blank=True)
	link = models.URLField(max_length=256,blank=True)
	rating = models.IntegerField(default=900)
	trynum = models.IntegerField(default=0)
	acnum = models.IntegerField(default=0)
	blognum = models.IntegerField(default=0)
	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.user.username)
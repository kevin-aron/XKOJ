from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder

class Tags(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = '文章标签'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name
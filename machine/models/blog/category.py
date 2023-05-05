from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder

class Category(models.Model):
	name = models.CharField(max_length=100)
	
	class Mate:
		verbose_name = '文章分类'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name
from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder

class Post(models.Model):
	title = models.CharField(max_length=200)
	writer = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	link = models.URLField('问题链接',default=-1)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '博客集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.title)
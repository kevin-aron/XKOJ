from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder

class Post(models.Model):
	title = models.CharField('博客题目', max_length=200)
	writer = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	idcode = models.CharField('博客路径',max_length=20,unique=True,default=1)
	link = models.URLField('博客链接',default=-1)
	content = models.TextField('博客内容')
	date_posted = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '博客集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.title)
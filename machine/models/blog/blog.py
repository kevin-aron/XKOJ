from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder
from machine.models.blog.category import Category
from machine.models.blog.tags import Tags

class Post(models.Model):
	title = models.CharField('博客题目', max_length=200)
	writer = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	idcode = models.CharField('博客路径',max_length=20,unique=True,default=1)
	link = models.URLField('博客链接',default=-1)
	excerpt = models.CharField('摘要',max_length=200,blank=True)
	content = models.TextField('博客内容')
	date_posted = models.DateTimeField('创建时间',auto_now_add=True)
	modeified_time = models.DateTimeField('修改时间',default=timezone.now)
	category = models.ForeignKey(Category,verbose_name='分类',null=True,on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tags,verbose_name='标签',null=True,blank=True)

	def save(self, *args, **kwargs):
		self.modeified_time = timezone.now()
		super().save(*args, **kwargs)
	class Meta:
		verbose_name = '博客集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.title)
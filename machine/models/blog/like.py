from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder
from machine.models.blog.blog import Post

class Like(models.Model):
	post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
	author = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)

	class Meta:
		unique_together = (('post','author'))
		verbose_name = '点赞集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.post)
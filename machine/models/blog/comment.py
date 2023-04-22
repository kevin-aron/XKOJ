from django.db import models
from django.utils import timezone
from machine.models.coder.coder import Coder
from machine.models.blog.blog import Post

class Comment(models.Model):
	post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
	author = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '评论集'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.post)
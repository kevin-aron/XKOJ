from django.db import models
from django.utils import timezone
from django.urls import reverse
from machine.models.problem.problem import Problem

def in_upload_path(instance, filename):
	return "/".join(["testcases", str(instance.problem.id)])+".in"
def out_upload_path(instance, filename):
	return "/".join(["testcases", str(instance.problem.id)])+".out"

class TestCase(models.Model):
	problem = models.ForeignKey(Problem, verbose_name='问题', on_delete=models.CASCADE)
	input_file = models.FileField('输入文件', upload_to=in_upload_path)
	output_file = models.FileField('输出文件', upload_to=out_upload_path)
	class Meta:
		verbose_name = '测试数据'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.problem)

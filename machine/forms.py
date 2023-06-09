from django import forms
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like
from machine.models.blog.category import Category
from machine.models.blog.tags import Tags

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = {'username', 'password'}

class ProblemForm(forms.ModelForm):
	name = forms.CharField()
	code = forms.CharField()
	statement = forms.CharField(widget = forms.Textarea(attrs={'class': 'markdown-editor'}))
	time_limit = forms.IntegerField()
	source = forms.CharField()
	input1 = forms.FileField()
	output1 = forms.FileField()
	class Meta:
		model = Problem
		fields = ['name','code','statement','time_limit','source','input1','output1']

class SubmissionForm(forms.ModelForm):
	langs = [("C","C"), ("CPP","C++"), ("JAVA","Java"), ("PYTH3","Python3")]
	lang = forms.ChoiceField(choices = langs)
	code = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Submission
		fields  = ['lang', 'code']

class BlogsForm(forms.ModelForm):
	title = forms.CharField(label='标题')
	excerpt = forms.CharField(label='摘要')
	content = forms.CharField(widget = forms.Textarea, label='正文')
	category = forms.ModelChoiceField(queryset=Category.objects.all(), label='分类')
	tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='标签', required=False)
	
	class Meta:
		model = Post
		fields = ['title', 'excerpt', 'content', 'category', 'tags']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', ]






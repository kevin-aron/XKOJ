from django import forms
from django.contrib.auth.models import User
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = {'username', 'password'}

class ProblemForm(forms.ModelForm):
	name = forms.CharField()
	code = forms.CharField()
	statement = forms.CharField(widget = forms.Textarea)
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


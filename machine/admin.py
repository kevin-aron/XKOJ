from django.contrib import admin
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission

admin.site.register(Coder)
admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Submission)

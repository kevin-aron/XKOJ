from django.contrib import admin
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem

admin.site.register(Coder)
admin.site.register(Problem)

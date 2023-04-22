from django.contrib import admin
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like

admin.site.register(Coder)
admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Submission)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)



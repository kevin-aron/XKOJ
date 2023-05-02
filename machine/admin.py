from django.contrib import admin
from machine.models.coder.coder import Coder
from machine.models.problem.problem import Problem
from machine.models.problem.testcase import TestCase
from machine.models.problem.submission import Submission
from machine.models.blog.blog import Post
from machine.models.blog.comment import Comment
from machine.models.blog.like import Like
from machine.models.game.game import Game
from machine.models.game.gameproblem import GameProblem
from machine.models.game.gamecoder import GameCoder
from machine.models.game.gamesubmission import GameSubmission
from machine.models.game.gamerk import GameRk

admin.site.register(Coder)
admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Submission)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Game)
admin.site.register(GameProblem)
admin.site.register(GameCoder)
admin.site.register(GameSubmission)
admin.site.register(GameRk)

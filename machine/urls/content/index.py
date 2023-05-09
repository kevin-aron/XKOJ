from django.urls import path,include
from django.conf.urls import url
from machine.views.content.allproblems import allproblems
from machine.views.content.viewproblem import viewproblem
from machine.views.content.submitcode import submitcode
from machine.views.content.viewsubmission import viewsubmission
from machine.views.content.crabug import crabug

urlpatterns=[
	path("problems/", allproblems, name="content_allproblems"),
	path("crabug/", crabug, name="content_crabug"), 
	url(r'^problems/(?P<pid>[\w\-]+)$', viewproblem, name="content_views"),
	url(r'^submit/(?P<pid>[\w\-]+)$', submitcode, name="content_submit"),
	url(r'^submission/(?P<submission_id>[\d]+)$', viewsubmission, name="content_viewssub"),
]
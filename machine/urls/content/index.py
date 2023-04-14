from django.urls import path,include
from machine.views.content.allproblems import allproblems

urlpatterns=[
	path("allproblems/", allproblems, name="content_allproblems"),
]
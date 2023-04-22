from django.urls import path,include
from django.conf.urls import url
from machine.views.blogs.viewblogs import viewblogs
urlpatterns=[
	path("blogs/", viewblogs, name="blogs_viewblogs"),
]
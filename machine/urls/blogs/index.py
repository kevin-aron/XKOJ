from django.urls import path,include
from django.conf.urls import url
from machine.views.blogs.viewblogs import viewblogs
from machine.views.blogs.showblog import showblog
from machine.views.blogs.addblog import addblog
from machine.views.blogs.about import about
from machine.views.blogs.bloglike import bloglike

urlpatterns=[
	path("about/", about, name="about"),
	path("blogs/", viewblogs, name="blogs_viewblogs"),
	path("addblog/", addblog, name="blogs_addblog"),
	url(r'^blogs/(?P<pid>[\w\-]+)$', showblog, name="blogs_showblog"),
	url(r'^bloglike/(?P<pid>[\w\-]+)$', bloglike, name="blogs_bloglike"),
]
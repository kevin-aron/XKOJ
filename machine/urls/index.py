from django.urls import path, include
from machine.views.index import index

urlpatterns = [
	path("", index, name="index"),
	path("settings/", include("machine.urls.settings.index")),
	path("content/", include("machine.urls.content.index")),
	path("blogs/", include("machine.urls.blogs.index")),
]
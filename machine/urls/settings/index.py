from django.urls import path,include
from machine.views.settings.register import register
from machine.views.settings.login import signin
from machine.views.settings.logout import signout

urlpatterns = [
	path("register/", register, name="settings_register"),
	path("login/", signin, name="settings_login"),
	path("logout/", signout, name="settings_logout"),
]
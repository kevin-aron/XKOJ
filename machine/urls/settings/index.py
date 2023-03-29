from django.urls import path,include
from machine.views.settings.register import register

urlpatterns = [
	path("register/", register, name="settings_register"),
]
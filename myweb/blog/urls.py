from django.urls import path

from django.conf import settings
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path("", views.index),
    path("about",views.about),
    path("moreinfo",views.moreinfo),
    path("style",views.style),
    path("singlepost",views.singlepost),
    path("login",views.login),
]
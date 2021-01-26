from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
	path("test", views.index, name="index"),
        path("gugu", views.gu),
       
        ]

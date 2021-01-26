from django.urls import path
from . import views

urlpatterns= [
        path('login', views.login),
        path('todo', views.index),
        path('signup', views.signup),
        path('login', views.login),
        path('logout', views.logout),
        path('members', views.login_after),
        path('<str:character1>/<str:character2>', views.my_novel, name='my_novel'),
        ]

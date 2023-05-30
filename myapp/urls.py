from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.hello),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks)
]

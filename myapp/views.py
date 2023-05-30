from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    title = 'Django course'
    return render(request, 'index.html')


def hello(request, username):
    return HttpResponse("<h2>Hello %s </h2>" % username)


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    return render(request, 'task.html')

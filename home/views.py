from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request,'home/home.html',context={})

def projects(request):
    model=Project.objects.all()
    return render (request,'home/projects.html',context={'project':model})

def view_project(request):
    return render (request,'home/aboutpro.html',context={})

def skills(request):
    return render(request, 'home/skills.html')
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('projects',views.projects,name='projects'),
    path('project',views.view_project,name='view_pro'),
    path('skills',views.skills,name='skills'),
]
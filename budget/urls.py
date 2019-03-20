from django.urls import path
from . import views

urlpatterns = [

    path('', views.project_list, name="project.list"),
    path('add', views.ProjectCreateView.as_view(), name="project.add"),
    path('<slug:project_slug>', views.project_detail, name="project.detail"),
]
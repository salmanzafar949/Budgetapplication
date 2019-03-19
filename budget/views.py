from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_list(request):
    return render(request, 'budget/project_list.html', {})


def project_detail(request, project_slug):
    ## fetching the correct project
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'budget/project_detail.html', {'project': project})

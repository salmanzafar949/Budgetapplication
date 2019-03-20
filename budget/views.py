from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Project, Category
from django.views.generic import CreateView
from django.utils.text import slugify
# Create your views here.

def project_list(request):
    return render(request, 'budget/project_list.html', {})


def project_detail(request, project_slug):
    ## fetching the correct project
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'budget/project_detail.html', {'project': project})

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/project_add.html'
    fields = ['name', 'budget']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')

        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name = category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])

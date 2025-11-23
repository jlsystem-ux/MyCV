from django.shortcuts import render, get_object_or_404
from .models import Project, Technology

def project_list(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()

    tech = request.GET.get('tech')
    if tech:
        projects = projects.filter(technologies__slug=tech)

    context = {
        'projects': projects,
        'technologies': technologies,
        'selected_tech': tech,
    }
    return render(request, 'portfolio/project_list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    related_projects = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(id=project.id).distinct()[:3]

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

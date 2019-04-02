from django.shortcuts import render, get_list_or_404
from .models import Project


# Create your views here.

def kickstarter_list_view(request):
    projects = get_list_or_404(Project, id__lte = 10)

    context = {
        'projects': projects,
    }

    return render(request, 'projects/list_view.html', context)

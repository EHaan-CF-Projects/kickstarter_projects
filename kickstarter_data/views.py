from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Project


# Create your views here.

def kickstarter_list_view(request):
    projects_list = get_list_or_404(Project)
    paginator =  Paginator(projects_list, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
    }

    return render(request, 'projects/list_view.html', context)

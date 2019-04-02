from django.shortcuts import render, get_list_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.

@cache_page(CACHE_TTL)
def kickstarter_list_view(request):
    projects_list = get_list_or_404(Project)
    paginator =  Paginator(projects_list, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
    }

    return render(request, 'projects/list_view.html', context)

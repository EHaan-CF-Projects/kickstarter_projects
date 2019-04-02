from django.urls import path
from .views import kickstarter_list_view

urlpatterns = [
    path('', kickstarter_list_view, name='home')
]
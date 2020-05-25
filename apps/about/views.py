from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
# Create your views here.
from django.views.generic import ListView
from .models import TeamExpert


class AboutView(ListView):
    template_name = 'about/about.html'  
    context_object_name = 'experts'           
    extra_context={
        'title':'About Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        queryset =  TeamExpert.objects.filter(status='p')
        return queryset

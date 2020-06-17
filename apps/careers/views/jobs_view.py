
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.
from django.views.generic import ListView,DetailView
from careers.models import Job
import django.utils.timezone as timezone

class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'job_id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        else:
            obj.viewed()
            self.object = obj
        return obj

    # def get_object(self, queryset=None):
    #     obj = super(JobDetailsView, self).get_object(queryset=queryset)
    #     if obj is None:
    #         raise Http404("Job doesn't exists")
    #     return obj

    def get_context_data(self, **kwargs):
        job_id = int(self.kwargs[self.pk_url_kwarg])
        user = self.request.user
        
        kwargs['next_job'] = self.object.next_job
        kwargs['prev_job'] = self.object.prev_job

        return super(JobDetailsView, self).get_context_data(**kwargs)

    # def get(self, request, *args, **kwargs):
    #     try:
    #         self.object = self.get_object()
    #     except Http404:
    #         # redirect here
    #         raise Http404("Job doesn't exists")
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)

class JobView(ListView):
    model = Job
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'
    extra_context = {
        'title': 'career'
    }
    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context



class SearchView(ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])




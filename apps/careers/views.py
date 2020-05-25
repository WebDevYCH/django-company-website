from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ApplyJobForm
from .models import JobCategory,Job,Applicant
from django.utils.decorators import method_decorator
import django.utils.timezone as timezone
# Create your views here.
class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

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

class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('home:home'))

    def get_success_url(self):
        return reverse_lazy('careers:job_description', kwargs={'id': self.kwargs['job_id'],'slug': self.slug})

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyJobView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['job'] = 1
    #     return kwargs

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class SearchView(ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])


class JobListView(ListView):
    model = Job
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5

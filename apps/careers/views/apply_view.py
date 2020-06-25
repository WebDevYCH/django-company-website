from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from careers.forms import ApplyJobForm, ApplicantDetailsForm
from careers.models import Job,Applicant, ApplicantDetails
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from uuslug import slugify
class JobApplyView(CreateView):
    template_name = 'jobs/create.html'
    form_class = ApplicantDetailsForm
    model = ApplicantDetails
    success_url = reverse_lazy('careers:careers')
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(self.request, *args, **kwargs)
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Ipsum` instance exists
        before going any further.
        """
        self.job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        applicant = ApplicantDetails.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super(JobApplyView, self).form_valid(form)

    def get_success_url(self):
        job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        slug = getattr(job, 'title')
        route_slug = slugify(slug)
        return reverse_lazy('careers:job_description', 
        kwargs={
            'job_id': self.kwargs['job_id'],
            'year': job.created_at.year,
            'month': job.created_at.month,
            'day': job.created_at.day,
            'slug': route_slug
            })

    def post(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        form = self.form_class(job, request.user,request.POST, request.FILES)
        self.object = None
        
        form = self.get_form()
        if form.is_valid():

            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        
        return render(request, 'jobs/create.html', {'form': form})

    def get_form_kwargs(self, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        kwargs = super(JobApplyView, self).get_form_kwargs(*args, **kwargs)
        #kwargs['job'] = self.kwargs['job_id']
        kwargs.update({'job': job,'user': self.request.user})
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(Job, pk=self.kwargs['job_id'])
        return context

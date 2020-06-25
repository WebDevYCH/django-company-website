
from django.http import Http404
# Create your views here.
from django.views.generic import ListView,DetailView
from django.contrib import messages
from careers.models import Job, ApplicantDetails
from django.utils.decorators import method_decorator
import django.utils.timezone as timezone
import logging
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
logger = logging.getLogger(__name__)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.auth import logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect

class LogoutIfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                logout(request)
                return self.handle_no_permission()
            return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

class ApplicantsDetailsView(PermissionRequiredMixin, LogoutIfNotStaffMixin, DetailView):
    permission_required = 'is_staff'
    model = ApplicantDetails
    template_name = 'jobs/admin/applicant_details.html'
    context_object_name = 'applicant'
    pk_url_kwarg = 'applicant_id'

    def get_object(self, queryset=None):
        obj = super(ApplicantsDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        else:
            self.object = obj
        return obj

    # def get_object(self, queryset=None):
    #     obj = super(JobDetailsView, self).get_object(queryset=queryset)
    #     if obj is None:
    #         raise Http404("Job doesn't exists")
    #     return obj

    def get_context_data(self, **kwargs):
        # kwargs['next_Applicant'] = self.object.next_job
        # kwargs['prev_Applicant'] = self.object.prev_job

        return super(ApplicantsDetailsView, self).get_context_data(**kwargs)


class ApplicantsperJobView(PermissionRequiredMixin, LogoutIfNotStaffMixin, ListView):
    permission_required = 'is_staff'
    model = ApplicantDetails
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 5

    def get_queryset(self):
        return ApplicantDetails.objects.filter(job_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=self.kwargs['job_id'])
        return context

class ApplicantsListView(PermissionRequiredMixin, LogoutIfNotStaffMixin, ListView):
    permission_required = 'is_staff'
    model = ApplicantDetails
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        # jobs = Job.objects.filter(user_id=self.request.user.id)
        return self.model.objects.filter()

class DashboardView(PermissionRequiredMixin, LogoutIfNotStaffMixin, ListView):
    permission_required = 'is_staff'
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)

@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    try:
        job = Job.objects.get(user_id=request.user.id, id=job_id)
        job.filled = True
        job.save()
    except IntegrityError as e:
        print(e.message)
        return HttpResponseRedirect(reverse_lazy('careers:employer-dashboard'))
    return HttpResponseRedirect(reverse_lazy('careers:employer-dashboard'))
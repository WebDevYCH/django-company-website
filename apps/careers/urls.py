from django.urls import path,include
from careers.views.admin_view import *
from careers.views.apply_view import *
from careers.views.jobs_view import *
from careers.apiview import JobsListing

app_name = "careers"
urlpatterns = [
    path('careers/', include([
        path("filter/", JobsListing.as_view(), name = 'listing'),
        path('', JobView.as_view(), name='careers'),
        path(r'<int:year>/<int:month>/<int:day>/<int:job_id>/<slug:slug>.html', JobDetailsView.as_view(), name='job_description'),
        path(r'applicants/<int:job_id>/job_apply.html', JobApplyView.as_view(), name='job_apply'),
        path('search', SearchView.as_view(), name='search'),
        path('employer/dashboard/', include([
            path('', DashboardView.as_view(), name='employer-dashboard'),
            path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
            path('applicants/<int:job_id>', ApplicantsperJobView.as_view(), name='employer-dashboard-applicants'),
            path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
        ])),
        path('admin/', include([
            path('applicant/<int:applicant_id>/<slug:slug>', ApplicantsDetailsView.as_view(), name='job_applicant_details'),
        ])),
    ])),
    # path('apply-job/<int:job_id>', careers.views.ApplyJobView.as_view(), name='apply-job'),
    
]
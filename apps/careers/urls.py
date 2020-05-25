from django.urls import path,include
from .views import *
app_name = "careers"
urlpatterns = [
    path('careers/', JobView.as_view(), name='careers'),
    path('job_details/<int:pk>/<slug:slug>/', JobDetailsView.as_view(), name='job_description'),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('search', SearchView.as_view(), name='search'),
    path('jobs', JobListView.as_view(), name='jobs'),
]
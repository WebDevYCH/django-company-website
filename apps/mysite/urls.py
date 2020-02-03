from django.urls import path,include
from apps.blog.views import IndexView
from .views import *
app_name = "mysite"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', IndexView.as_view(), name='blogs'),
    path('contact/', contact, name='contact'),
    path('careers/', JobView.as_view(), name='careers'),
    path('services/', services, name='services'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('portfolio-single/<int:pk>/<slug:slug>/', contact, name='portfolio-single'),
    path('single-blog/', contact, name='single-blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>/', article, name='article'),
    path('job_details/<int:pk>/<slug:slug>/', JobDetailsView.as_view(), name='job_description'),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    
]
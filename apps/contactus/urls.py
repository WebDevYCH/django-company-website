from django.urls import path,include
from .views import *
app_name = "contactus"
urlpatterns = [
    path('contact/', contact, name='contact'),
]
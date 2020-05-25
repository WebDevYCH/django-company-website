from django.urls import path,include
from .views import *
app_name = "services"
urlpatterns = [

    path('services/', services, name='services'),
    
]
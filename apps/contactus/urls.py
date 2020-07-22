from django.urls import path,include
from .views import *
from .apiview import *
app_name = "contactus"
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('newsletter/', EmailSubscribeView.as_view(), name='newsletter'),
]
from django.urls import path,include
from .views import *
app_name = "about"
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]
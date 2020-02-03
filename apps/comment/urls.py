from django.urls import path
from .views import *

app_name="comment"

urlpatterns = [
    path('update_comment', update_comment, name ='update_comment'),
]


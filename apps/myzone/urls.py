from django.urls import path
from .views import TalkView

app_name = "myzone"

urlpatterns = [
    path('talk/', TalkView.as_view(), name='talk'),
]

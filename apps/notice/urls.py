from django.urls import path
from .views import *

app_name = "notice"

urlpatterns = [
    path('my_notifications/', my_notifications, name="my_notifications"),
    path('my_notification/<int:my_notifications_pk>', my_notification, name="my_notification"),
    path('delete_my_read_notifications', delete_my_read_notifications, name="delete_my_read_notifications"),
]

# -*- coding: utf-8 -*-
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
import xadmin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from werobot.contrib.django import make_view
from apps.accounts import views

urlpatterns = [
    # add your own patterns here
    path('admin/', xadmin.site.urls, name="admin"),
    path('mdeditor/', include('mdeditor.urls')),
    path('comment/', include('apps.comment.urls')),
    path('', include('apps.notice.urls')),
    path('', include('apps.myzone.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', include('apps.mysite.urls')),
    path('', include('apps.blog.urls')),
    path('search/', include('haystack.urls')),
    path('api/', include([
        path('', include('apps.mysite.api.urls')),
    ])),
    
]  + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
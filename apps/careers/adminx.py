# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

class JobAdmin(object):

    list_display = ['id', 'user', 'title','slug','last_date','location']
    search_fields = ['name','role','title','location']
    list_filter = ['id', 'title', 'created_at', 'status','last_date',]
    
    model_icon = 'fa fa-user'
   
    ordering = ['-id']

    readonly_field = ['views','created_at']

    exclude = ['views','created_at']

    list_display_link = ['name','created_at']

    # style_fields = {'body':'ueditor'}
class JobCategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'

class ApplicantAdmin(object):
    list_display = ['id','user','job']
    search_fields = ['job']
    model_icon = 'fa fa-file-text'
    
xadmin.site.register(Applicant,ApplicantAdmin)
xadmin.site.register(JobCategory,JobCategoryAdmin)
xadmin.site.register(Job,JobAdmin)

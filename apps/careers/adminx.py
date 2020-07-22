# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views
from django_summernote.widgets import SummernoteWidget
from django import forms

class JobForm(forms.ModelForm):
    # body = forms.CharField(widget=AdminPagedownWidget())
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Job
        fields = '__all__'

class JobAdmin(object):

    form = JobForm
    list_display = ['id', 'user', 'title','last_date','location']
    search_fields = ['name','role','title','location','description']
    list_filter = ['id', 'title', 'created_at', 'status','last_date',]
    
    model_icon = 'fa fa-user'
   
    ordering = ['-id']

    readonly_field = ['views','created_at']

    exclude = ['views','created_at']

    list_display_link = ['name','created_at']

    # style_fields = {'body':'ueditor'}
class JobCategoryAdmin(object):
    list_display = ['id','name','is_active']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'
    
class JobLocationAdmin(object):
    list_display = ['id','location','is_active']
    search_fields = ['location']
    model_icon = 'fa fa-file-text'

class ApplicantDetailsAdmin(object):
    list_display = ['fullname','email','phone']
    search_fields = ['fullname','email']
    model_icon = 'fa fa-file-text'

class ApplicantAdmin(object):
    list_display = ['id','user','job']
    search_fields = ['job']
    model_icon = 'fa fa-file-text'
    
xadmin.site.register(Applicant,ApplicantAdmin)
xadmin.site.register(JobCategory,JobCategoryAdmin)
xadmin.site.register(JobLocation,JobLocationAdmin)
xadmin.site.register(Job,JobAdmin)
xadmin.site.register(ApplicantDetails,ApplicantDetailsAdmin)
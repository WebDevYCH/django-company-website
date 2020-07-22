# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

class ContactAdmin(object):


    list_display = ['username', 'email']
    search_fields = ['username','subject']
    list_filter = ['id', 'created_at']
    
    model_icon = 'fab fa-inbox'
   
    ordering = ['-id']

    exclude = ['created_at']

class NewsletterAdmin(object):


    list_display = ['email']
    
    model_icon = 'fa fa-envelope'
   
    ordering = ['-id']

    exclude = ['created_at']
xadmin.site.register(MailBook,NewsletterAdmin)
xadmin.site.register(Contact,ContactAdmin)
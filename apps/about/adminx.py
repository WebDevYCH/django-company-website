# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views


class TeamExpertAdmin(object):

    list_display = ['id', 'name', 'role', 'about', 'facebook','twitter','instagram','linkedin','github']
    search_fields = ['name','role']
    list_filter = ['id', 'name', 'created_time', 'status']
    
    model_icon = 'fa fa-user'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['views','created_time']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['name','created_time']

    # style_fields = {'body':'ueditor'}

xadmin.site.register(TeamExpert,TeamExpertAdmin)

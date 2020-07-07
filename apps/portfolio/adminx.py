# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

class PortfolioAdmin(object):
    # 展示的字段
    list_display = ['id', 'title','status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_at', 'status']
    # 修改图标
    model_icon = 'fa fa-briefcase'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['views','created_at']

    list_display_link = ['title']
xadmin.site.register(Portfolio,PortfolioAdmin)


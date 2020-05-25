# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

class PostAdmin(object):
    # 展示的字段
    list_display = ['id', 'title', 'created_time', 'category', 'status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_time', 'category', 'status']
    # 修改图标
    model_icon = 'fa fa-file-text'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['title']

    # style_fields = {'body':'ueditor'}


class CategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'


class TagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'



xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)


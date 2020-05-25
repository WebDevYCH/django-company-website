# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

class PortfolioAdmin(object):
    # 展示的字段
    list_display = ['id', 'title','slug' ,'status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_time', 'status']
    # 修改图标
    model_icon = 'fa fa-briefcase'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['title']
xadmin.site.register(Portfolio,PortfolioAdmin)
class MeanListAdmin(object):
    list_display = ['id', 'title', 'link', 'icon', 'status']
    search_field = ['title']
    model_icon = 'fa fa-list'


class MessagesAdmin(object):
    list_display = ['id', 'name']
    model_icon = 'fa fa-commenting'


xadmin.site.register(MeanList,MeanListAdmin)
xadmin.site.register(Messages,MessagesAdmin)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = 'AGroSite'
    site_footer = '2019'

    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )
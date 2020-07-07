# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views


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
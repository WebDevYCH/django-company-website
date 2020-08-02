# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views
from django.conf import settings

from cookie_consent.models import (
    Cookie,
    CookieGroup,
    LogItem,
)


class CookieAdmin(object):
    list_display = ('varname', 'name', 'cookiegroup', 'path', 'domain',
                    'get_version')
    search_fields = ('name', 'domain', 'cookiegroup__varname',
                     'cookiegroup__name')
    readonly_fields = ('varname',)
    list_filter = ('cookiegroup',)


class CookieGroupAdmin(object):
    list_display = ('varname', 'name', 'is_required', 'is_deletable',
                    'get_version')
    search_fields = ('varname', 'name',)
    list_filter = ('is_required', 'is_deletable',)


class LogItemAdmin(object):
    list_display = ('action', 'cookiegroup', 'version', 'created')
    list_filter = ('action', 'cookiegroup')
    readonly_fields = ('action', 'cookiegroup', 'version', 'created')
    date_hierarchy = 'created'


xadmin.site.register(Cookie, CookieAdmin)
xadmin.site.register(CookieGroup, CookieGroupAdmin)
if settings.COOKIE_CONSENT_LOG_ENABLED:
    xadmin.site.register(LogItem, LogItemAdmin)

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
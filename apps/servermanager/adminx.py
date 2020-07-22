# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

from .models import commands, EmailSendLog


class CommandsAdmin(object):
    list_display = ('title', 'command', 'describe')


class EmailSendLogAdmin(object):
    list_display = ('title', 'emailto', 'send_result', 'created_time')
    readonly_fields = ('title', 'emailto', 'send_result', 'created_time', 'content')

    def has_add_permission(self,request):
        return False

xadmin.site.register(commands, CommandsAdmin)
xadmin.site.register(EmailSendLog, EmailSendLogAdmin)

from django.utils.html import mark_safe
from django.utils.translation import pgettext_lazy

from .models import Like
from .utils import admin_change_url
import xadmin

class LikeAdmin(object):
    list_filter = (
        "timestamp",
    )
    list_display = (
        "sender",
        "content_object_link",
        "timestamp"
    )
    list_select_related = (
        "sender",
    )
    raw_id_fields = (
        'sender',
    )
    readonly_fields = (
        'timestamp',
    )
    search_fields = (
        "sender__username",
        "sender__email",
        "sender__first_name",
        "sender__last_name"
    )

    def content_object_link(self, obj):
        if obj.content_object:
            url = admin_change_url(obj.content_object)
            return mark_safe(
                f'<a href="{url}" target="_blank">{obj.content_object}</a>'
            )
        return '-'
    content_object_link.short_description = (
        pgettext_lazy('like', 'Content object')
    )
xadmin.site.register(Like, LikeAdmin)
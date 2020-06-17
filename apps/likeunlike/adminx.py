
from django.utils.html import mark_safe
from django.utils.translation import pgettext_lazy

from .models import AgroLike
from agroutils.contenttype import admin_change_url
import xadmin

class AgroLikeAdmin(object):
    list_filter = (
        "created_at",
    )
    list_display = (
        "sender",
        "content_object_link",
        "created_at"
    )
    list_select_related = (
        "sender",
    )
    raw_id_fields = (
        'sender',
    )
    readonly_fields = (
        'created_at',
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
xadmin.site.register(AgroLike, AgroLikeAdmin)
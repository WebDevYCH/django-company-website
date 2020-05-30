#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: feed.py
@time: 2016/12/22 下午10:16
"""

from django.contrib.syndication.views import Feed
from blog.models import Article
from django.conf import settings
from django.utils.feedgenerator import Rss201rev2Feed
from agrosite.utils import CommonMarkdown
from django.contrib.auth import get_user_model
from datetime import datetime


class AgrositeFeed(Feed):
    feed_type = Rss201rev2Feed

    description = 'Daqiao without work, Epee without edge.'
    title = "And listen to Fengyin, great skill without work, great sword without edge."
    link = "/feed/"

    def author_name(self):
        return get_user_model().objects.first().username

    def author_link(self):
        return get_user_model().objects.first().get_absolute_url()

    def items(self):
        return Article.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return CommonMarkdown.get_markdown(item.body)

    def feed_copyright(self):
        now = datetime.now()
        return "Copyright© {year} 且听风吟".format(year=now.year)

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return

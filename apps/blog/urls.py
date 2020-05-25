#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2016/11/2 下午7:15
"""

from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

app_name = "blog"
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'npage/<int:page>/', views.IndexView.as_view(), name='index_page'),

    path(r'narticle/<int:year>/<int:month>/<int:day>/<int:article_id>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid'),

    path(r'ncategory/<slug:category_name>.html', views.CategoryDetailView.as_view(), name='category_detail'),
    path(r'ncategory/<slug:category_name>/<int:page>.html', views.CategoryDetailView.as_view(),
         name='category_detail_page'),

    path(r'nauthor/<author_name>.html', views.AuthorDetailView.as_view(), name='author_detail'),
    path(r'nauthor/<author_name>/<int:page>.html', views.AuthorDetailView.as_view(),
         name='author_detail_page'),

    path(r'ntag/<slug:tag_name>.html', views.TagDetailView.as_view(), name='tag_detail'),
    path(r'ntag/<slug:tag_name>/<int:page>.html', views.TagDetailView.as_view(), name='tag_detail_page'),
    path('archives.html', cache_page(60 * 60)(views.ArchivesView.as_view()), name='archives'),
    path('links.html', views.LinkListView.as_view(), name='links'),
    path(r'nupload', views.fileupload, name='upload'),
    path(r'nrefresh', views.refresh_memcache, name='refresh')

]

#!/usr/bin/env python
# encoding: utf-8


from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

app_name = "blog"
urlpatterns = [
    path(r'blogs.html', views.IndexView.as_view(), name='index'),
    path(r'npage/<int:page>/', views.IndexView.as_view(), name='index_page'),

    path(r'article/<int:year>/<int:month>/<int:day>/<int:article_id>/<slug:slug>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid'),

    path(r'category/<slug:category_name>.html', views.CategoryDetailView.as_view(), name='category_detail'),
    path(r'category/<slug:category_name>/<int:page>.html', views.CategoryDetailView.as_view(),
         name='category_detail_page'),

    path(r'author/<author_name>.html', views.AuthorDetailView.as_view(), name='author_detail'),
    path(r'author/<author_name>/<int:page>.html', views.AuthorDetailView.as_view(),
         name='author_detail_page'),

    path(r'tag/<slug:tag_name>.html', views.TagDetailView.as_view(), name='tag_detail'),
    path(r'tag/<slug:tag_name>/<int:page>.html', views.TagDetailView.as_view(), name='tag_detail_page'),
    path(r'archives.html', cache_page(60 * 60)(views.ArchivesView.as_view()), name='archives'),
    path(r'links.html', views.LinkListView.as_view(), name='links'),
    path(r'upload', views.fileupload, name='upload'),
    path(r'refresh', views.refresh_memcache, name='refresh')

]

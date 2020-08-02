#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: blog_tags.py
@time: 2016/11/2 下午11:10
"""

from django import template
from django.db.models import Q
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import random
from django.urls import reverse
from blog.models import Article, Category, Tag, Links, SideBar
from django.utils.encoding import force_text
from django.shortcuts import get_object_or_404
import hashlib
import urllib
from agrosite.utils import cache_decorator, cache
from django.contrib.auth import get_user_model
from agrosite.utils import get_current_site
import logging
from comment.models import Comment
from comment.form import CommentForm
from django.contrib.contenttypes.models import ContentType

logger = logging.getLogger(__name__)

register = template.Library()
from django.core.files.images import get_image_dimensions
from bs4 import BeautifulSoup as BS

@register.simple_tag
def timeformat(data):
    try:
        return data.strftime(settings.TIME_FORMAT)
        # print(data.strftime(settings.TIME_FORMAT))
        # return "ddd"
    except Exception as e:
        logger.error(e)
        return ""

@register.simple_tag
def markdown_images(content):
    
    lst_images = list()
    soup = BS(content, "html.parser")
    for imgtag in soup.find_all('img'):
        if '.jpg' in imgtag['src'] or '.png' in imgtag['src']:
                lst_images.append(imgtag['src'])
    
    return lst_images

@register.simple_tag
def datetimeformat(data):
    try:
        return data.strftime(settings.DATE_TIME_FORMAT)
    except Exception as e:
        logger.error(e)
        return ""


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    from agrosite.utils import CommonMarkdown
    return mark_safe(CommonMarkdown.get_markdown(content))


@register.filter(is_safe=True)
@stringfilter
def truncatechars_content(content):
    """
    Get a summary of the content of the article
    :param content:
    :return:
    """
    from django.template.defaultfilters import truncatechars_html
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()
    return truncatechars_html(content, blogsetting.article_sub_length)


@register.filter(is_safe=True)
@stringfilter
def truncate(content):
    
    from django.utils.html import strip_tags
    
    return strip_tags(content)[:250]

@register.inclusion_tag('blog/tags/breadcrumb.html')
def load_breadcrumb(article):
    """
    Get article breadcrumbs
    :param article:
    :return:
    """
    names = article.get_category_tree()
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()
    site = get_current_site().domain
    names.append((blogsetting.sitename, '/'))
    names = names[::-1]

    return {
        'names': names,
        'title': article.title
    }


@register.inclusion_tag('blog/tags/article_tag_list.html')
def load_articletags(article):
    """
    Article tags
    :param article:
    :return:
    """
    tags = article.tags.all()
    tags_list = []
    for tag in tags:
        url = tag.get_absolute_url()
        count = tag.get_article_count()
        tags_list.append((
            url, count, tag, random.choice(settings.BOOTSTRAP_COLOR_TYPES)
        ))
    return {
        'article_tags_list': tags_list
    }


@register.inclusion_tag('blog/tags/sidebar.html')
def load_sidebar(user, linktype):
    """
    Load the sidebar
    :return:
    """
    logger.info('load sidebar')
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()
    recent_articles = Article.objects.filter(status='p', is_removed=False)[:blogsetting.sidebar_article_count]
    sidebar_categorys = Category.objects.all()
    extra_sidebars = SideBar.objects.filter(is_enable=True).order_by('sequence')
    most_read_articles = Article.objects.filter(status='p', is_removed=False).order_by('-views')[:blogsetting.sidebar_article_count]
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    links = Links.objects.filter(is_enable=True).filter(Q(show_type=str(linktype)) | Q(show_type='a'))
    commment_list = Comment.objects.filter().order_by('-id')[:blogsetting.sidebar_comment_count]
    # Tag Cloud Calculate font size
    # Calculate the average value based on the total number, the size is (number / average value) * step
    increment = 5
    tags = Tag.objects.all()
    sidebar_tags = None
    if tags and len(tags) > 0:
        s = [t for t in [(t, t.get_article_count()) for t in tags] if t[1]]
        count = sum([t[1] for t in s])
        dd = 1 if (count == 0 or not len(tags)) else count / len(tags)
        import random
        sidebar_tags = list(map(lambda x: (x[0], x[1], (x[1] / dd) * increment + 10), s))
        random.shuffle(sidebar_tags)

    return {
        'recent_articles': recent_articles,
        'sidebar_categorys': sidebar_categorys,
        'most_read_articles': most_read_articles,
        'article_dates': dates,
        'sidebar_comments': commment_list,
        'user': user,
        'sidabar_links': links,
        'show_google_adsense': blogsetting.show_google_adsense,
        'google_adsense_codes': blogsetting.google_adsense_codes,
        'open_site_comment': blogsetting.open_site_comment,
        'show_gongan_code': blogsetting.show_gongan_code,
        'sidebar_tags': sidebar_tags,
        'extra_sidebars': extra_sidebars
    }


@register.inclusion_tag('blog/tags/article_meta_info.html')
def load_article_metas(article, user, is_detail):
    """
    Get article meta information
    :param article:
    :return:
    """
    return {
        
        'article': article,
        'user': user,
        'is_detail' : is_detail
    }


@register.inclusion_tag('blog/tags/article_pagination.html')
def load_pagination_info(page_obj, page_type, tag_name):
    previous_url = ''
    next_url = ''
    if page_type == '':
        if page_obj.has_next():
            next_number = page_obj.next_page_number()
            next_url = reverse('blog:index_page', kwargs={'page': next_number})
        if page_obj.has_previous():
            previous_number = page_obj.previous_page_number()
            previous_url = reverse('blog:index_page', kwargs={'page': previous_number})
    if page_type == 'Category Tag Archive':
        tag = get_object_or_404(Tag, name=tag_name)
        if page_obj.has_next():
            next_number = page_obj.next_page_number()
            next_url = reverse('blog:tag_detail_page', kwargs={'page': next_number, 'tag_name': tag.slug})
        if page_obj.has_previous():
            previous_number = page_obj.previous_page_number()
            previous_url = reverse('blog:tag_detail_page', kwargs={'page': previous_number, 'tag_name': tag.slug})
    if page_type == 'Author Article Archive':
        if page_obj.has_next():
            next_number = page_obj.next_page_number()
            next_url = reverse('blog:author_detail_page', kwargs={'page': next_number, 'author_name': tag_name})
        if page_obj.has_previous():
            previous_number = page_obj.previous_page_number()
            previous_url = reverse('blog:author_detail_page', kwargs={'page': previous_number, 'author_name': tag_name})

    if page_type == 'Catalog archive':
        category = get_object_or_404(Category, name=tag_name)
        if page_obj.has_next():
            next_number = page_obj.next_page_number()
            next_url = reverse('blog:category_detail_page',
                               kwargs={'page': next_number, 'category_name': category.slug})
        if page_obj.has_previous():
            previous_number = page_obj.previous_page_number()
            previous_url = reverse('blog:category_detail_page',
                                   kwargs={'page': previous_number, 'category_name': category.slug})

    return {
        'previous_url': previous_url,
        'next_url': next_url,
        'page_obj': page_obj
    }


"""
@register.inclusion_tag('nav.html')
def load_nav_info():
    category_list = Category.objects.all()
    return {
        'nav_category_list': category_list
    }
"""


@register.inclusion_tag('blog/tags/article_info.html')
def load_article_detail(article, isindex, user):
    """
    Load article details
    : param article:
    : param isindex: Whether the list page, if the list page only displays the summary
    :return:
    """
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()

    return {
        'article': article,
        'isindex': isindex,
        'user': user,
        'open_site_comment': blogsetting.open_site_comment,
    }

@register.inclusion_tag('blog/tags/article_detail_info.html')
def load_article_detail_info(article, isindex, user):
    """
    Load article details
    :param article:
    :param isindex:Whether the list page, if the list page only displays the summary
    :return:
    """
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()

    return {
        'article': article,
        'isindex': isindex,
        'user': user,
        'open_site_comment': blogsetting.open_site_comment,
    }




@register.simple_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)

@register.simple_tag
def get_comment_count(article):
    content_type = ContentType.objects.get_for_model(article)
    return Comment.objects.filter(content_type=content_type,object_id=article.id).count()

@register.simple_tag
def load_related_articles(article, user, slug, tags):
    """
    Load article details
    : param article:
    : param isindex: Whether the list page, if the list page only displays the summary
    :return:
    """
    from itertools import chain
    category = get_object_or_404(Category, slug=slug)
    categoryname = article.category.name
    categoryname = categoryname
    categorynames = list(map(lambda c: c.name, category.get_sub_categorys()))
    category_list = Article.objects.filter(category__name__in=categorynames, status='p', is_removed=False)
    print(category_list)
    for tag in tags:
        tags_list = Article.objects.filter(tags__name=tag, type='a', status='p', is_removed=False)
    result = list(set(chain(category_list,tags_list)))
    return result




@register.inclusion_tag('blog/tags/article_comment_form.html')
def load_comment_form(article):
    content_type = ContentType.objects.get_for_model(article)
    comment_form = CommentForm(initial={'content_type': content_type.model, 'object_id': article.pk, 'reply_comment_id': '0'})
    return  {'comment_form':comment_form}
    

@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_comment_id': '0'})
    return form

@register.inclusion_tag('blog/tags/article_comment.html')
def load_comments_list(article):
    content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=content_type, object_id=article.id, parent=None).order_by('-comment_time')  # 获取所有与此类型相同的评论
    return {
        'comments': comments,
    }
from home.models import *
from setting.models import *
from django import template
from django.db.models import Count
from comment.models import Comment
from comment.form import CommentForm
from django.contrib.contenttypes.models import ContentType
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])


@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False

@register.simple_tag
def get_posts_tags():
    tags = Tag.objects.annotate(posts_count=Count('post')).order_by('-posts_count')[:14]
    return tags



@register.simple_tag
def get_category():
    categories = Category.objects.annotate(category_count=Count('post')).order_by('-category_count')[:10]
    return categories


@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type,object_id=obj.id).count()



@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_comment_id': '0'})
    return form



@register.simple_tag
def get_comments_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.id, parent=None).order_by('-comment_time')  # 获取所有与此类型相同的评论
    return comments


@register.simple_tag
def get_meanList():
    means = MeanList.objects.all().order_by('pk')
    return means


@register.simple_tag
def get_category_id(category_name):
    category = Category.objects.get(name=category_name)
    return category.id


@register.simple_tag
def get_seo_info():
    try:
        seo_info = Seo.objects.get(id=1)
        return seo_info
    except Seo.DoesNotExist:
        return None


@register.simple_tag
def get_friend_links():
    links = FriendLinks.objects.all()
    return links


@register.simple_tag
def get_custom_code():
    try:
        custom_code = CustomCode.objects.get(id=1)
        return custom_code
    except CustomCode.DoesNotExist:
        return None


@register.simple_tag
def get_site_info():
    try:
        site_info = SiteInfo.objects.get(id=1)
        return site_info
    except SiteInfo.DoesNotExist:
        return None


@register.simple_tag
def get_social_media():
    try:
        social_media = Social.objects.get(id=1)
        return social_media
    except Social.DoesNotExist:
        return None

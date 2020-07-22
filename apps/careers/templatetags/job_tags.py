
from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse
from careers.models import Job, JobCategory, ApplicantDetails,JobLocation
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger(__name__)

register = template.Library()



@register.inclusion_tag('blog/tags/job_meta_info.html')
def load_job_metas(job, user):
    """
    Get job meta information
    :param job:
    :return:
    """
    return {
        'job': job,
        'user': user
    }


# @register.inclusion_tag('blog/tags/job_pagination.html')
# def load_pagination_info(page_obj, page_type, tag_name):
#     previous_url = ''
#     next_url = ''
#     if page_type == '':
#         if page_obj.has_next():
#             next_number = page_obj.next_page_number()
#             next_url = reverse('careers:index_page', kwargs={'page': next_number})
#         if page_obj.has_previous():
#             previous_number = page_obj.previous_page_number()
#             previous_url = reverse('careers:index_page', kwargs={'page': previous_number})
    
#     if page_type == 'Author job Archive':
#         if page_obj.has_next():
#             next_number = page_obj.next_page_number()
#             next_url = reverse('careers:author_detail_page', kwargs={'page': next_number, 'author_name': tag_name})
#         if page_obj.has_previous():
#             previous_number = page_obj.previous_page_number()
#             previous_url = reverse('careers:author_detail_page', kwargs={'page': previous_number, 'author_name': tag_name})

#     if page_type == 'Catalog archive':
#         category = get_object_or_404(JobCategory, name=tag_name)
#         if page_obj.has_next():
#             next_number = page_obj.next_page_number()
#             next_url = reverse('careers:category_detail_page',
#                                kwargs={'page': next_number, 'category_name': category.slug})
#         if page_obj.has_previous():
#             previous_number = page_obj.previous_page_number()
#             previous_url = reverse('careers:category_detail_page',
#                                    kwargs={'page': previous_number, 'category_name': category.slug})

#     return {
#         'previous_url': previous_url,
#         'next_url': next_url,
#         'page_obj': page_obj
#     }


"""
@register.inclusion_tag('nav.html')
def load_nav_info():
    category_list = Category.objects.all()
    return {
        'nav_category_list': category_list
    }
"""


@register.inclusion_tag('jobs/tags/job_base.html')
def load_jobs_baseinfo(job, user, isdetail):
    """
    Load job details
    : param job:
    : param isindex: Whether the list page, if the list page only displays the summary
    :return:
    """
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()

    return {
        'job': job,
        'user': user,
        'isdetail': isdetail,
        'open_site_comment': blogsetting.open_site_comment,
    }

@register.inclusion_tag('jobs/tags/job_filters.html')
def load_job_filters():
    job_categorys = JobCategory.objects.filter(is_active=True).order_by('name')
    job_location = JobLocation.objects.filter(is_active=True).order_by('location')
    return {
        'job_categorys': job_categorys,
        'job_locations' : job_location,
    }

@register.inclusion_tag('jobs/tags/job_applicants.html')
def load_job_applicants(applicant):
    return {
        'applicant': applicant,
    }
    
@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = ApplicantDetails.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False

@register.inclusion_tag('jobs/tags/job_details.html')
def load_job_detail_info(job, user):
    """
    Load job details
    :param job:
    :param isindex:Whether the list page, if the list page only displays the summary
    :return:
    """
    from agrosite.utils import get_blog_setting
    blogsetting = get_blog_setting()

    return {
        'job': job,
        'user': user,
        'open_site_comment': blogsetting.open_site_comment,
    }

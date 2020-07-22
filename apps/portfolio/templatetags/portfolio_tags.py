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
from django.template.defaultfilters import stringfilter
import logging

logger = logging.getLogger(__name__)

register = template.Library()


@register.inclusion_tag('portfolio/tags/portfolio_card.html')
def load_portfolio_card(portfolio):
    
    return {
        'portfolio': portfolio,
    }

@register.inclusion_tag('portfolio/tags/portfolio_modal.html')
def load_portfolio_modal(portfolio):

    return {
        'portfolio': portfolio,
        
    }






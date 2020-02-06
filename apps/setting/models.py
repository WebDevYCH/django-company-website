from django.db import models
import django.utils.timezone as timezone


class FriendLinks(models.Model):
    name = models.CharField('Site name', max_length = 50, default = 'Eastbound notebook')
    link = models.CharField('Website address', max_length = 200, default = 'https: //www.eastnotes.com')

    class Meta:
        verbose_name = "Links"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


class Seo(models.Model):
    title = models.CharField("Site Master Name", max_length = 100, default = 'DjangoEast')
    sub_title = models.CharField("Site name for website", max_length = 200, default = 'DjangoEast')
    description = models.CharField("Site description", max_length = 200, default = 'DjangoEast')
    keywords = models.CharField("Keyword", max_length = 200, default = 'DjangoEast')

    class Meta:
        verbose_name = "SEO Set up"
        verbose_name_plural = verbose_name


class CustomCode(models.Model):
    statistics = models.TextField("Website Statistics Code ", default = 'Statistics Code')

    class Meta:
        verbose_name = "Custom code"
        verbose_name_plural = verbose_name


class SiteInfo(models.Model):
    created_time = models.DateField("Website time", default = timezone.now)
    record_info = models.CharField("Record information", max_length = 100, default = 'Record number')
    development_info = models.CharField("Development information", max_length = 100, default = 'Development information')
    arrange_info = models.CharField("Deployment Information", max_length = 100, default = 'Deployment Information')

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = verbose_name

class Social(models.Model):
    github = models.URLField("Github address", max_length=200, default='https://github.com/mxdshr/DjangoEast')
    wei_bo = models.URLField("Weibo address", max_length=200, default='https://weibo.com/')
    zhi_hu = models.URLField("Know the address", max_length=200, default='https://www.zhihu.com/people/sylax8/')
    qq = models.CharField("QQ number", max_length=20, default='783342105')
    wechat = models.CharField("WeChat",max_length=50,default='reborn0502')
    official_wechat = models.CharField("WeChat public account", max_length=50, default='Programmer Xiangdong')

    class Meta:
        verbose_name = "Social account"
        verbose_name_plural = verbose_name

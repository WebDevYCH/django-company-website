import logging
from abc import ABCMeta, abstractmethod, abstractproperty

from django.db import models
from django.urls import reverse
from django.conf import settings
from uuslug import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from agrosite.utils import get_current_site
from agrosite.utils import cache_decorator, cache
from django.utils.timezone import now
from mdeditor.fields import MDTextField
from django.contrib.auth import get_user_model
User = get_user_model()
logger = logging.getLogger(__name__)
from django.utils.html import strip_tags



LINK_SHOW_TYPE =(
    ('i', 'Home'),
    ('l', 'List page'),
    ('p', 'Article page'),
    ('a', 'Total Station'),
    ('s', 'Friendly Link Page'),
)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('create time', default = now)
    last_mod_time = models.DateTimeField('modified time', default = now)
    is_removed = models.BooleanField('Is Removed', default=False)
    
    def save(self, *args, **kwargs):
        is_update_views = isinstance(self, Article) and 'update_fields' in kwargs and kwargs['update_fields'] == [
            'views']
        if is_update_views:
            Article.objects.filter(pk=self.pk).update(views=self.views)
        else:
            if 'slug' in self.__dict__:
                slug = getattr(self, 'title') if 'title' in self.__dict__ else getattr(self, 'name')
                setattr(self, 'slug', slugify(slug))
            super().save(*args, **kwargs)

    def get_full_url(self):
        site = get_current_site().domain
        url = "https://{site}{path}".format(site=site, path=self.get_absolute_url())
        return url

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass



class Article(BaseModel):
    """article"""
    STATUS_CHOICES =(
        ('d', 'Draft'),
        ('p', 'Publish'),
    )
    COMMENT_STATUS =(
        ('o', 'Open'),
        ('c', 'Close'),
    )
    TYPE =(
       ('a', 'article'),
       ('p', 'page'),
    )
    title = models.CharField('title', max_length=200, unique=True)
    body = models.TextField('content')
    pub_time = models.DateTimeField('publish time', blank=False, null=False, default=now)
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICES, default='p')
    comment_status = models.CharField('comment_status', max_length=1, choices=COMMENT_STATUS, default='o')
    type = models.CharField('type', max_length=1, choices=TYPE, default='a')
    views = models.PositiveIntegerField('views', default=0)
    author = models.ForeignKey(User, verbose_name='author', blank=False, null=False,
                               on_delete=models.CASCADE)
    article_order = models.IntegerField('article order', blank=False, null=False, default=0)
    category = models.ForeignKey('Category', verbose_name='category', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField('Tag', verbose_name='tags', blank=True)
    audio = models.CharField("audiofile path", max_length=150)

    def body_to_string(self):
        return self.body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-article_order', '-pub_time']
        verbose_name = "Article"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def get_absolute_url(self):
        slug = getattr(self, 'title') if 'title' in self.__dict__ else getattr(self, 'name')
        route_slug = slugify(slug)
        return reverse('blog:detailbyid', kwargs={
            'article_id': self.id,
            'year': self.created_time.year,
            'month': self.created_time.month,
            'day': self.created_time.day,
            'slug': route_slug
        })

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        tree = self.category.get_category_tree()
        names = list(map(lambda c:(c.name, c.get_absolute_url()), tree))

        return names

    
    def save(self, *args, **kwargs):
        
        self.audio = settings.MEDIA_URL+'audio/'+ slugify(self.title) + '.mp3'
        super().save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def comment_list(self):
        cache_key = 'article_comments_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get article comments:{id}'.format(id=self.id))
            return value
        

    def get_admin_url(self):
        info =(self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @cache_decorator(expiration=60 * 100)
    def next_article(self):
        # Next
        return Article.objects.filter(id__gt=self.id, status='p', is_removed=False).order_by('id').first()

    @cache_decorator(expiration=60 * 100)
    def prev_article(self):
        # previous
        return Article.objects.filter(id__lt=self.id, status='p', is_removed=False).first()


class Category(BaseModel):
    """Article Classification"""
    name = models.CharField('name', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name="parent category", blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "category"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'category_name': self.slug})

    def __str__(self):
        return self.name

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        """
        Recursively get the parent of the catalog
        :return: 
        """
        categorys = []

        def parse(category):
            categorys.append(category)
            if category.parent_category:
                parse(category.parent_category)

        parse(self)
        return categorys

    @cache_decorator(60 * 60 * 10)
    def get_sub_categorys(self):
        """
        Get all subsets of the current catalog
        :return: 
        """
        categorys = []
        all_categorys = Category.objects.all()

        def parse(category):
            if category not in categorys:
                categorys.append(category)
            childs = all_categorys.filter(parent_category=category)
            for child in childs:
                if category not in categorys:
                    categorys.append(child)
                parse(child)

        parse(self)
        return categorys

class Tag(BaseModel):
    """Article Label"""
    name = models.CharField('name', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'tag_name': self.slug})

    @cache_decorator(60 * 60 * 10)
    def get_article_count(self):
        return Article.objects.filter(tags__name=self.name, is_removed=False).distinct().count()

    class Meta:
        ordering = ['name']
        verbose_name = "tags"
        verbose_name_plural = verbose_name


class Links(models.Model):
    """Links"""

    name = models.CharField('name', max_length=30, unique=True)
    link = models.URLField('link')
    sequence = models.IntegerField('sequence', unique=True)
    is_enable = models.BooleanField('is_enable', default=True, blank=False, null=False)
    show_type = models.CharField('show type', max_length=1, choices=LINK_SHOW_TYPE, default='i')
    created_time = models.DateTimeField('created time', default=now)
    last_mod_time = models.DateTimeField('modified time', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'Links'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SideBar(models.Model):
    """Sidebar, you can display some html content"""
    name = models.CharField('name', max_length=100)
    content = models.TextField("content")
    sequence = models.IntegerField('sequence', unique=True)
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('created time', default=now)
    last_mod_time = models.DateTimeField('modified time', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'Sidebar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogSettings(models.Model):
    '' 'Site Settings' ''
    sitename = models.CharField("sitename", max_length=200, null=False, blank=False, default='')
    site_description = models.TextField("site_description", max_length=1000, null=False, blank=False, default='')
    site_seo_description = models.TextField("site_seo_description", max_length=1000, null=False, blank=False, default='')
    site_keywords = models.TextField("site_keywords", max_length=1000, null=False, blank=False, default='')
    article_sub_length = models.IntegerField("article_sub_length", default=200)
    sidebar_article_count = models.IntegerField("sidebar_article_count", default=10)
    sidebar_comment_count = models.IntegerField("sidebar_comment_count", default=5)
    show_google_adsense = models.BooleanField('Whether to display Google ads', default = False)
    google_adsense_codes = models.TextField('advertising content', max_length = 2000, null = True, blank = True, default = '')
    open_site_comment = models.BooleanField('Whether to open the website comment function', default = True)
    beiancode = models.CharField('Record number', max_length = 2000, null = True, blank = True, default = '')
    analyticscode = models.TextField("Site Statistics Code", max_length = 1000, null = False, blank = False, default = '')
    show_gongan_code = models.BooleanField('Whether to display the public security record number', default = False, null = False)
    gongan_beiancode = models.TextField('Public Security Record Number', max_length = 2000, null = True, blank = True, default = '')
    resource_path = models.CharField("static file save address", max_length = 300, null = False, default = '/var/www/resource/')
    class Meta:
        verbose_name = 'Website configuration'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if BlogSettings.objects.exclude(id=self.id).count():
            raise ValidationError(_('There can only be one configuration'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from agrosite.utils import cache
        cache.clear()

class Speech(models.Model):
    text = models.TextField(max_length=2000)
    language = models.TextField(max_length=50)
    file_name = models.TextField(max_length=1000)
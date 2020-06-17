# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField
from django.contrib.auth import get_user_model
User = get_user_model()
class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='Category Name')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Article Category"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blogs:category', kwargs={'pk': self.pk})


class Tag(models.Model):
	
	name = models.CharField('Label name',max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Article tags"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blogs:tag_list', kwargs={'pk': self.pk})


class Post(models.Model):

	
	PUBLISH_STATUS = (
		('p', 'Article Page'),
		('c', 'Tutorial page'),
		('d', 'Draft Box'),
		('r', 'Recycle Bin'),
	)

	STICK_STATUS = (
		('y', 'Sticky'),
		('n', 'Do not top'),
	)

	title = models.CharField ('Title', max_length = 100, unique = True)
	slug = models.SlugField('Slug', max_length = 200,  unique = True)
	body = MDTextField('body')
	created_time = models.DateTimeField('Creation time', auto_now = True)
	modified_time = models.DateTimeField('Modified time', auto_now = True)
	excerpt = models.CharField('Summary', max_length = 200, blank = True,)
	views = models.PositiveIntegerField('Views', default = 0)
	words = models.PositiveIntegerField('Word count', default = 0)
	category = models.ForeignKey(Category, verbose_name = 'Article Category', on_delete = models.CASCADE)
	tag = models.ManyToManyField(Tag, verbose_name = 'Tag type', blank = True)
	# author = models.ForeignKey (User, verbose_name = 'Author', on_delete = models.CASCADE, default = "reborn")
	author = models.ForeignKey(User, verbose_name = 'Author', on_delete = models.CASCADE)
	status = models.CharField('Article status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
	stick = models.CharField('Whether sticky', max_length = 1, choices = STICK_STATUS, default = 'n')

	def get_absolute_url(self):
		return reverse('blogs:post', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	def get_user(self):
		return self.author

	
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.body).replace("&nbsp;", "").replace("#", "")[:150]
		self.words = len(strip_tags(self.body).replace(" ", "").replace('\n', ""))
		super(Post, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Add article"
		verbose_name_plural = verbose_name
		ordering = ['-created_time']



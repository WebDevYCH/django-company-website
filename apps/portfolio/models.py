from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
from abc import ABCMeta, abstractmethod, abstractproperty
from uuslug import slugify
from agrosite.utils import cache_decorator, cache
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseModel(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField('create time', auto_now_add=True)
	modified_at = models.DateTimeField('modified time', auto_now=True)
	
	def save(self, *args, **kwargs):
		is_update_views = isinstance(self, Portfolio) and 'update_fields' in kwargs and kwargs['update_fields'] == [
			'views']
		if is_update_views:
			Portfolio.objects.filter(pk=self.pk).update(views=self.views)
		else:
			if 'slug' in self.__dict__:
				slug = getattr(self, 'title') if 'title' in self.__dict__ else getattr(self, 'name')
				setattr(self, 'slug', slugify(slug))
			super().save(*args, **kwargs)

class Portfolio(BaseModel):

	PUBLISH_STATUS = (
		('p', 'Article Page'),
		('c', 'Tutorial page'),
		('d', 'Draft Box'),
		('r', 'Recycle Bin'),
	)

	title = models.CharField ('Title', max_length = 100, unique = True)
	about =  models.TextField("About")
	cover = models.ImageField("Upload cover", upload_to = 'portfolio', blank = True)
	views = models.PositiveIntegerField('Views', default = 0)
	words = models.PositiveIntegerField('Word count', default = 0)
	author = models.ForeignKey(User, verbose_name = 'Author', on_delete = models.CASCADE)
	status = models.CharField('Article status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
	
	def get_absolute_url(self):
		slug = getattr(self, 'title') if 'title' in self.__dict__ else getattr(self, 'name')
		route_slug = slugify(slug)
		return reverse('portfolio:single_portfolio', kwargs={
			'portfolio_id': self.id,
			'year': self.created_at.year,
			'month': self.created_at.month,
			'day': self.created_at.day,
			'slug': route_slug
		})


	def body_to_string(self):
		return self.description

	def __str__(self):
		return self.title

	def viewed(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		super(Portfolio, self).save(*args, **kwargs)

	def get_admin_url(self):
		info =(self._meta.app_label, self._meta.model_name)
		return reverse('admin:%s_%s_change' % info, args=(self.pk,))

	@cache_decorator(expiration=60 * 100)
	def next_portfolio(self):
		# Next
		return Portfolio.objects.filter(id__gt=self.id, PUBLISH_STATUS='p').order_by('id').first()

	@cache_decorator(expiration=60 * 100)
	def prev_portfolio(self):
		# previous
		return Portfolio.objects.filter(id__lt=self.id, PUBLISH_STATUS='p').first()

	class Meta:
		verbose_name = "Add Portfolio"
		verbose_name_plural = verbose_name
		ordering = ['-created_at']
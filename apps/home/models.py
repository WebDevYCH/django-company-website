from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField
# Create your models here.
class Messages(models.Model):
	name = models.CharField(max_length=100,verbose_name="leave me a message")
	admin = models.ForeignKey(User,verbose_name='Webmaster',on_delete=models.CASCADE,blank=True,null=True)

	def get_absolute_url(self):
		return reverse('blogs:messages')

	def get_user(self):
		return self.admin

	class Meta:
		verbose_name = "Website message"
		verbose_name_plural = verbose_name


class MeanList(models.Model):

	STATUS = (
		('y', 'Show'),
		('n', 'Hide'),
	)

	title = models.CharField("menu name", max_length = 100)
	link = models.CharField("Menu Link", max_length = 100, blank = True, null = True,)
	icon = models.CharField("menu icon", max_length = 100, blank = True, null = True,)
	status = models.CharField('Display status', max_length = 1, choices = STATUS, default = 'y')

	class Meta:
		verbose_name = "Menu Bar"
		verbose_name_plural = verbose_name

class Portfolio(models.Model):

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
	excerpt = models.CharField('Summary', max_length = 200, blank = True,)
	content =  MDTextField('content')
	cover = models.ImageField("Upload cover", upload_to = 'portfolio', blank = True)
	created_time = models.DateTimeField('Creation time', auto_now = True)
	modified_time = models.DateTimeField('Modified time', auto_now = True)
	views = models.PositiveIntegerField('Views', default = 0)
	words = models.PositiveIntegerField('Word count', default = 0)
	author = models.ForeignKey(User, verbose_name = 'Author', on_delete = models.CASCADE)
	status = models.CharField('Article status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
	stick = models.CharField('Whether sticky', max_length = 1, choices = STICK_STATUS, default = 'n')

	def get_absolute_url(self):
		return reverse('mysite:portfolio-single', kwargs={'pk': self.pk,'slug': self.slug})

	def __str__(self):
		return self.title

	def get_user(self):
		return self.author

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		
		super(Portfolio, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Add Portfolio"
		verbose_name_plural = verbose_name
		ordering = ['-created_time']
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField

# 创建博文分类的表
class JobCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name='Category Name')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Job Category"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('mysite:careers', kwargs={'pk': self.pk})

class Job(models.Model):
	JOB_TYPE = (
		('1', "Full time"),
		('2', "Part time"),
		('3', "Internship"),
	)
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
	user = models.ForeignKey(User,verbose_name = 'CreatedBy',on_delete=models.CASCADE)
	title = models.CharField('title',max_length=300)
	slug = models.SlugField('Slug', max_length = 200,  unique = True)
	cover = models.ImageField("Upload cover", upload_to = 'job')
	description = MDTextField('description')
	location = models.CharField('Location',max_length=150)
	jobtype = models.CharField('JobType',choices=JOB_TYPE, max_length=10)
	jobcategory = models.ForeignKey(JobCategory, verbose_name = 'Job_Category', on_delete = models.CASCADE)
	last_date = models.DateTimeField('LastDate',default=timezone.now)
	created_at = models.DateTimeField('CreatedAt',default=timezone.now)
	filled = models.BooleanField('Filled',default=False)
	salary = models.IntegerField('Salary',default=0, blank=True)
	views = models.PositiveIntegerField('Views', default = 0)
	status = models.CharField('Article status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
	stick = models.CharField('Whether sticky', max_length = 1, choices = STICK_STATUS, default = 'n')

	def get_absolute_url(self):
		return reverse('mysite:job_description', kwargs={'pk': self.pk,'slug': self.slug})

	def __str__(self):
		return self.title

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		super(Job, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Add Job"
		verbose_name_plural = verbose_name
		ordering = ['-created_at']
	
class Applicant(models.Model):
    user = models.ForeignKey(User,verbose_name = 'Applicant', on_delete=models.CASCADE)
    job = models.ForeignKey(Job,verbose_name = 'Job', on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField('AppliedOn',default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()

class TeamExpert(models.Model):

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

	name = models.CharField ('Name', max_length = 100, unique = True)
	role = models.CharField('Role', max_length = 200,)
	about =  models.TextField('About')
	cover = models.ImageField("Upload cover", upload_to = 'portfolio')
	facebook = models.URLField("Facebook",max_length=250, blank = True)
	twitter = models.URLField("Twitter",max_length=250, blank = True)
	instagram = models.URLField("Instagram",max_length=250, blank = True)
	linkedin = models.URLField("Linkedin",max_length=250, blank = True)
	github = models.URLField("Github",max_length=250, blank = True)
	created_time = models.DateTimeField('Creation time', auto_now = True)
	modified_time = models.DateTimeField('Modified time', auto_now = True)
	views = models.PositiveIntegerField('Views', default = 0)
	words = models.PositiveIntegerField('Word count', default = 0)
	status = models.CharField('Article status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
	stick = models.CharField('Whether sticky', max_length = 1, choices = STICK_STATUS, default = 'n')

	def __str__(self):
		return self.name

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		super(TeamExpert, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Add TeamExpert"
		verbose_name_plural = verbose_name
		ordering = ['-created_time']

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

class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='Category Name')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Article Category"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:category', kwargs={'pk': self.pk})


class Tag(models.Model):
	# name是标签名的字段
	name = models.CharField('Label name',max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Article tags"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:tag_list', kwargs={'pk': self.pk})


# 创建文章的类
class Post(models.Model):

	# 发表状态
	PUBLISH_STATUS = (
		('p', 'Article Page'),
		('c', 'Tutorial page'),
		('d', 'Draft Box'),
		('r', 'Recycle Bin'),
	)

	# 是否置顶
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
		return reverse('mysite:article', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	def get_user(self):
		return self.author

	# 阅读量增加1
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


class BookCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="Category Name")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Book list classification"
		verbose_name_plural = verbose_name


class BookTag(models.Model):
	name = models.CharField(max_length=100, verbose_name="label")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:book_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "Book list label"
		verbose_name_plural = verbose_name


class Book(models.Model):
	name = models.CharField("Book Title", max_length = 100)
	author = models.CharField("Author", max_length = 100)
	category = models.ForeignKey(BookCategory, on_delete = models.CASCADE, verbose_name = "book category")
	tag = models.ManyToManyField(BookTag, verbose_name = "Book Tag")
	cover = models.ImageField("cover image", upload_to = 'books', blank = True)
	score = models.DecimalField("Douban score", max_digits = 2, decimal_places = 1)
	created_time = models.DateField("Add time", null = True, default = timezone.now)
	time_consuming = models.CharField("Reading initial time", max_length = 100)
	pid = models.CharField("Article ID", max_length = 100, blank = True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pid})

	class Meta:
		verbose_name = "Add book"
		verbose_name_plural = verbose_name
		ordering = ['-pk']


class MovieCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="Movie classification")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Movie classification"
		verbose_name_plural = verbose_name


class MovieTag(models.Model):
	name = models.CharField(max_length=100,verbose_name="Label name",blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:movie_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "Movie label"
		verbose_name_plural = verbose_name


class Movie(models.Model):
	name = models.CharField("movie name", max_length = 100)
	director = models.CharField("Director", max_length = 100)
	actor = models.CharField("Starring", max_length = 100)
	category = models.ForeignKey(MovieCategory, on_delete = models.CASCADE, verbose_name = "Movie Category")
	tag = models.ManyToManyField(MovieTag, verbose_name = "Movie Tag")
	cover = models.ImageField("Upload cover", upload_to = 'movies', blank = True)
	score = models.DecimalField("Douban score", max_digits = 2, decimal_places = 1)
	release_time = models.DateField("release time")
	created_time = models.DateField("Add time", default = timezone.now)
	length_time = models.PositiveIntegerField("Movie Duration", default = 0)
	watch_time = models.DateField("watch time", default = timezone.now)
	pid = models.CharField("Article ID", max_length = 100, blank = True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:post', kwargs={'pk': self.pid})

	class Meta:
		verbose_name = "Add movie"
		verbose_name_plural = verbose_name
		ordering = ['-pk']


class Messages(models.Model):
	name = models.CharField(max_length=100,verbose_name="leave me a message")
	admin = models.ForeignKey(User,verbose_name='Webmaster',on_delete=models.CASCADE,blank=True,null=True)

	def get_absolute_url(self):
		return reverse('blog:messages')

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


class Courses(models.Model):
	title = models.CharField("Tutorial name", max_length = 100)
	cover = models.ImageField("Upload cover", upload_to = 'course', blank = True)
	category = models.CharField("Tutorial Category", max_length = 100)
	introduce = models.CharField("Tutorial Introduction", max_length = 200, blank = True)
	status = models.CharField("Update status", max_length = 50)
	article = models.ManyToManyField(Post, verbose_name = "tutorial article", blank = True)
	created_time = models.DateTimeField('Creation time', null = True, default = timezone.now)
	# author = models.ForeignKey (User, verbose_name = 'Author', on_delete = models.DO_NOTHING, default = "reborn")
	author = models.ForeignKey(User, verbose_name = 'Author', on_delete = models.DO_NOTHING)
	comments = models.PositiveIntegerField("Number of comments", default = 0)
	numbers = models.PositiveIntegerField("Number of tutorials", default = 0)
	views = models.PositiveIntegerField("Views", default = 0)

	class Meta:
		verbose_name = "List of tutorials"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:course', kwargs={'pk': self.pk})

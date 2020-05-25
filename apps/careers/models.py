# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField

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

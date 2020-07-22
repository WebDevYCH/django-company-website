# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.urls import reverse
import django.utils.timezone as timezone
from django.contrib.auth import get_user_model
from abc import ABCMeta, abstractmethod, abstractproperty
import logging
from uuslug import slugify
from agrosite.utils import get_current_site
from agrosite.utils import cache_decorator, cache
from .file_validation_field import ContentTypeRestrictedFileField
from django.core.validators import RegexValidator

User = get_user_model()
logger = logging.getLogger(__name__)
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('create time', auto_now_add=True)
    modified_at = models.DateTimeField('modified time', auto_now=True)
    
    def save(self, *args, **kwargs):
        is_update_views = isinstance(self, Job) and 'update_fields' in kwargs and kwargs['update_fields'] == [
            'views']
        if is_update_views:
            Job.objects.filter(pk=self.pk).update(views=self.views)
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

class JobCategory(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Category Name')
    user = models.ForeignKey(User,verbose_name ='Created By', on_delete=models.CASCADE)
    is_active = models.BooleanField("Is Active", default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('careers:careers', kwargs={'pk': self.pk})

class JobLocation(BaseModel):
    location = models.CharField(max_length=100, verbose_name='location')
    user = models.ForeignKey(User,verbose_name ='Created By', on_delete=models.CASCADE)
    is_active = models.BooleanField("Is Active", default=True)
    def __str__(self):
        return self.location

    class Meta:
        verbose_name = "Job Location"
        verbose_name_plural = verbose_name

class Job(BaseModel):
    JOB_TYPE = (
        ('1', "Full time"),
        ('2', "Part time"),
        ('3', "Internship"),
        ('4', "Remote"),
        ('5', "Freelance"),
    )
    PUBLISH_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft Box'),
        ('r', 'Recycle Bin'),
    )

    STICK_STATUS = (
        ('y', 'Sticky'),
        ('n', 'Do not top'),
    )
    
    title = models.CharField('title',max_length=300)
    cover = models.ImageField("Upload cover", upload_to = 'job')
    description = models.TextField('Description')
    location = models.ForeignKey(JobLocation, verbose_name = 'Job_Location', on_delete = models.CASCADE)
    jobtype = models.CharField('JobType',choices=JOB_TYPE, max_length=10)
    jobcategory = models.ForeignKey(JobCategory, verbose_name = 'Job_Category', on_delete = models.CASCADE)
    last_date = models.DateTimeField('LastDate',default=timezone.now)
    filled = models.BooleanField('Filled',default=False)
    salary = models.IntegerField('Salary',default=0, blank=True)
    views = models.PositiveIntegerField('Views', default = 0)
    vacancies = models.PositiveIntegerField('Number of Vaccencies', default = 0)
    status = models.CharField('Job status', max_length = 1, choices = PUBLISH_STATUS, default = 'p')
    stick = models.CharField('Whether sticky', max_length = 1, choices = STICK_STATUS, default = 'n')
    user = models.ForeignKey(User,verbose_name = 'CreatedBy',on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        slug = getattr(self, 'title') if 'title' in self.__dict__ else getattr(self, 'name')
        route_slug = slugify(slug)
        return reverse('careers:job_description', kwargs={
            'job_id': self.id,
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
        super(Job, self).save(*args, **kwargs)

    def get_admin_url(self):
        info =(self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @cache_decorator(expiration=60 * 100)
    def next_job(self):
        # Next
        return Job.objects.filter(id__gt=self.id, PUBLISH_STATUS='p').order_by('id').first()

    @cache_decorator(expiration=60 * 100)
    def prev_job(self):
        # previous
        return Job.objects.filter(id__lt=self.id, PUBLISH_STATUS='p').first()

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

class ApplicantDetails(BaseModel):
    COLLEGE = (
        ('p', 'Puc'),
        ('d', 'Diploma'),
    )
    DEGREE_MARKS = (
        ('g', 'Grade'),
        ('p', 'Percentage'),
    )
    job = models.ForeignKey(Job, verbose_name="Job Selected", on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name = 'CreatedBy',on_delete=models.CASCADE)
    fullname = models.CharField("Fullname", max_length=100)
    cover = models.ImageField("Upload cover", upload_to = 'job/coverphoto/')
    email = models.EmailField("Email", max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    github_regex = RegexValidator(regex=r'^https:\/\/[a-z]{2,3}\.github\.com\/.*$',
                                 message="Url must be entered in the format: 'https://github.com/xxx or https://www.github.com/xxx '. Up to 15 digits allowed.")
    linkedin_regex = RegexValidator(regex=r'^https:\/\/[a-z]{2,3}\.linkedin\.com\/.*$',
                                     message="Phone number must be entered in the format: 'https://linkedin.com/in/xxx or https://www.linkedin.com/in/xxx'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    tenth_percent = models.FloatField("Tenth Percent")
    puc_or_diploma = models.CharField('College', max_length = 1, choices = COLLEGE, default = 'd')
    puc_or_diploma_marks = models.FloatField("Puc or Diploma Marks")
    board = models.CharField("Board", max_length=60)
    degree_college = models.CharField("Degree College", max_length=50)
    location = models.CharField("Location", max_length=50)
    university = models.CharField("University", max_length=50)
    branch = models.CharField("Branch", max_length=50)
    grade_or_percent = models.CharField('Degree Marks Format', max_length = 1, choices = DEGREE_MARKS, default = 'g')
    degree_marks = models.FloatField("Degree Marks")
    github = models.URLField("Github Url", max_length=100,validators=[github_regex], blank = True)
    linkedin = models.URLField("Linkedin Url", max_length=100,validators=[linkedin_regex], blank = True)
    resume = ContentTypeRestrictedFileField('Resume',upload_to='documents/%Y/%m/%d', help_text = 'Attach resume with .docx or .pdf format', content_types=['application/pdf','application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],max_upload_size=5242880)
    
    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        slug = getattr(self, 'fullname') if 'fullname' in self.__dict__ else getattr(self, 'fullname')
        route_slug = slugify(slug)
        return reverse('careers:job_applicant_details', kwargs={
            'applicant_id':self.id,
            'slug': route_slug,
        })
    
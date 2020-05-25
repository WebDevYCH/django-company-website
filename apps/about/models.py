from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

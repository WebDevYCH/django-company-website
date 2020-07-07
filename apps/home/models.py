from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

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


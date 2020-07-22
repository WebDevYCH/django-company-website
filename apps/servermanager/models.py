from django.db import models


# Create your models here.
class commands(models.Model):
    title = models.CharField('title', max_length=300)
    command = models.CharField('command', max_length=2000)
    describe = models.CharField('description', max_length=300)
    created_time = models.DateTimeField('createdaAt', auto_now_add=True)
    last_mod_time = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Commands'
        verbose_name_plural = verbose_name


class EmailSendLog(models.Model):
    emailto = models.CharField('Emailto', max_length=300)
    title = models.CharField('title', max_length=2000)
    content = models.TextField('content')
    send_result = models.BooleanField('send result', default=False)
    created_time = models.DateTimeField('created time', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Email Sendlog'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

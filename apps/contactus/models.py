from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Contact(models.Model):
    username = models.CharField("Full Name", max_length=50)
    email = models.EmailField("Your Email", max_length=254)
    subject = models.CharField("Subject", max_length=250)
    message = models.TextField("Enter Message")
    created_at = models.DateTimeField('created At',default=timezone.now)

    def __str__(self):
        return self.username

class MailBook(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    is_active = models.BooleanField("Is Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def mail_exists(self, request):
        return self.objects.filter(email = request.email).exists()
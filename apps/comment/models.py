from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
User = get_user_model()
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, verbose_name = "comment source")
    object_id = models.PositiveIntegerField("Comment Object")
    content_object = GenericForeignKey('content_type', 'object_id')
    text = RichTextField("Comment Content")
    comment_time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "comment user")
    root = models.ForeignKey('self', related_name = 'root_comment', null = True, on_delete = models.CASCADE)
    parent = models.ForeignKey('self', related_name = 'parent_comment', null = True, on_delete = models.CASCADE)
    reply_to = models.ForeignKey(User, related_name = 'replies', null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = verbose_name
        ordering = ['-comment_time']

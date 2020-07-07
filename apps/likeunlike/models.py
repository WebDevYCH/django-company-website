from typing import Tuple

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils import timezone


User = get_user_model()

class Like(models.Model):
    """
    Like model
    """
    sender = models.ForeignKey(
        User,
        verbose_name=pgettext_lazy("like", "sender"),
        related_name="likes",
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=pgettext_lazy('like', 'Content type')
    )
    object_id = models.CharField(
        pgettext_lazy('like', 'Object id'),
        max_length=50
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        unique_together = (
            (
                "sender",
                "content_type",
                "object_id"
            ),
        )
        verbose_name = pgettext_lazy('like', 'Like')
        verbose_name_plural = pgettext_lazy('like', 'Likes')

    def __str__(self) -> str:
        return f"{self.sender} - {self.content_object}"

    @classmethod
    def like(
            cls,
            sender: User,
            content_type: ContentType,
            object_id: str
    ) -> Tuple['Like', bool]:
        """
        Class method to like-dislike object
        """
        obj, created = cls.objects.get_or_create(
            sender=sender,
            content_type=content_type,
            object_id=object_id
        )
        if not created:
            obj.delete()
        return obj, created

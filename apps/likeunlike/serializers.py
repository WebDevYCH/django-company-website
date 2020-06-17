from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import pgettext_lazy

from rest_framework import serializers
from .models import Like
from agroutils.contenttype import allowed_content_type
from .services import send_signals
from .serializers import GenericObjectRelatedField
from django.conf import settings as django_setting


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for AgroLike model
    """
    content_object = GenericObjectRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class LikeToggleSerializer(serializers.ModelSerializer):
    """
    Serializer to like element
    """
    id = serializers.CharField(write_only=True)
    content_type = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=ContentType.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'content_type']

    def validate_content_type(self, value):
        if not allowed_content_type(value):
            raise serializers.ValidationError(
                pgettext_lazy('like', 'Not allowed content type')
            )
        return value

    def validate(self, data):
        content_type = data['content_type']
        try:
            obj = content_type.get_object_for_this_type(pk=data['id'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                pgettext_lazy('like', 'Object not found.')
            )
        else:
            data['object'] = obj
        return data

    def create(self, validated_data):
        like, created = Like.like(
            self.context['request'].user,
            validated_data['content_type'],
            validated_data['object'].pk
        )
        send_signals(
            created=created,
            request=self.context['request'],
            like=like,
            obj=validated_data['object']
        )
        return like


class IsLikedSerializer(serializers.Serializer):
    """
    Serializer to return liked objects
    """
    ids = serializers.ListField(
        child=serializers.CharField()
    )
    content_type = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=ContentType.objects.all()
    )

    def validate(self, data):
        liked_ids = list(
            Like.objects
            .filter(
                content_type=data['content_type'],
                object_id__in=data['ids'],
                sender=self.context['request'].user
            ).values_list('id', flat=True)
        )
        data['ids'] = liked_ids
        return data


from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import pgettext_lazy

from rest_framework import serializers
from .models import Like
from .utils import allowed_content_type
from .services import send_signals
from django.conf import settings
from django.apps import apps
from django.utils.module_loading import import_string
class GenericObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `liked_object` generic relationship.
    """

    def to_representation(self, value):
        serializers_map = {}

        for model_path, serializer_data in settings.LIKES_MODELS.items():
            app_label, model_name = model_path.split('.')
            serializer_path = serializer_data.get('serializer')

            if all([app_label, model_name, serializer_path]):
                model_class = apps.get_model(app_label, model_name)
                serializer_class = import_string(serializer_path)
                serializers_map[model_class] = serializer_class

        for model in serializers_map.keys():
            if isinstance(value, model):
                return serializers_map[model](
                    instance=value,
                    context=self.context
                ).data

        return str(value)

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


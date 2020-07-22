from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import pgettext_lazy

from rest_framework import serializers
from .models import MailBook

class EmailSubscribeSerializer(serializers.ModelSerializer):
    """
    Serializer to like element
    """
    
    email = serializers.CharField(write_only=True)
    
    class Meta:
        model = MailBook
        fields = ['email']

    def validate_email(self, value):
        
        if MailBook.objects.filter(email=value,is_active=True).exists():
            raise serializers.ValidationError(
                pgettext_lazy('email', 'email already exists')
            )
        return value


    def create(self, validated_data):
        return MailBook.objects.create(**validated_data)





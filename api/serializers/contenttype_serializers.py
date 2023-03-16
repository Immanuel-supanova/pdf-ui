from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class ContentTypeSerializers(serializers.ModelSerializer):
    """This is a serializer for ContentType Model"""

    class Meta:
        model = ContentType
        fields = '__all__'

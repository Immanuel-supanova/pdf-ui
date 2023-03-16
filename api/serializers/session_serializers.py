from django.contrib.sessions.models import Session
from rest_framework import serializers


class SessionSerializers(serializers.ModelSerializer):
    """This is a serializer for Session Model"""

    class Meta:
        model = Session
        fields = '__all__'

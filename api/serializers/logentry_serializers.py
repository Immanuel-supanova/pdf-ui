from django.contrib.admin.models import LogEntry
from rest_framework import serializers


class LogEntrySerializers(serializers.ModelSerializer):
    """This is a serializer for LogEntry Model"""

    class Meta:
        model = LogEntry
        fields = '__all__'

from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializers(serializers.ModelSerializer):
    """This is a serializer for Permissions Model"""

    class Meta:
        model = Permission
        fields = '__all__'

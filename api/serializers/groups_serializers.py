from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """This is a serializer for Group Model"""

    class Meta:
        model = Group
        fields = '__all__'

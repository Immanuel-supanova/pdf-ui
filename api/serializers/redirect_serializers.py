from django.contrib.redirects.models import Redirect
from rest_framework import serializers


class RedirectSerializers(serializers.ModelSerializer):
    """This is a serializer for Redirect Model"""

    class Meta:
        model = Redirect
        fields = '__all__'

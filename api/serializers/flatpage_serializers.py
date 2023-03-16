from django.contrib.flatpages.models import FlatPage
from rest_framework import serializers


class FlatPageSerializers(serializers.ModelSerializer):
    """This is a serializer for FlatPage Model"""

    class Meta:
        model = FlatPage
        fields = "__all__"

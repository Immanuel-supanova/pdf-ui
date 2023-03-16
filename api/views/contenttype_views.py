from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import ContentTypeSerializers


class ContentTypeList(generics.ListAPIView):
    """
    ContentTypeList lists all contenttype entities
    """

    serializer_class = ContentTypeSerializers
    queryset = ContentType.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class ContentTypeRetrieve(generics.RetrieveAPIView):
    """
    ContentTypeRetrieve is used to retrieve individual contenttypes from the database
    """

    serializer_class = ContentTypeSerializers
    queryset = ContentType.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

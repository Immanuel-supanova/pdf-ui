from django.contrib.flatpages.models import FlatPage
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import FlatPageSerializers


class FlatPageList(generics.ListAPIView):
    """
    FlatPageList lists all FlatPage entities
    """

    serializer_class = FlatPageSerializers
    queryset = FlatPage.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class FlatPageRetrieve(generics.RetrieveAPIView):
    """
    FlatPageRetrieve is used to retrieve individual flatpages from the database
    """

    serializer_class = FlatPageSerializers
    queryset = FlatPage.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

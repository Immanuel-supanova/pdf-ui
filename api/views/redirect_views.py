from django.contrib.redirects.models import Redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import RedirectSerializers


class RedirectList(generics.ListAPIView):
    """
    RedirectList lists all Redirect entities
    """

    serializer_class = RedirectSerializers
    queryset = Redirect.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class RedirectRetrieve(generics.RetrieveAPIView):
    """
    RedirectRetrieve is used to retrieve individual redirects from the database
    """

    serializer_class = RedirectSerializers
    queryset = Redirect.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

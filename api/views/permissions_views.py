from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import PermissionSerializers


class PermissionList(generics.ListAPIView):
    """
    PermissionList lists all Permission entities
    """

    serializer_class = PermissionSerializers
    queryset = Permission.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class PermissionRetrieve(generics.RetrieveAPIView):
    """
    PermissionRetrieve is used to retrieve individual permission from the database
    """

    serializer_class = PermissionSerializers
    queryset = Permission.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

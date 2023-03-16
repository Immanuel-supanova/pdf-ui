from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import GroupSerializer


class GroupList(generics.ListAPIView):
    """
    GroupList lists all Groups entities
    """

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class GroupRetrieve(generics.RetrieveAPIView):
    """
    GroupRetrieve is used to retrieve individual groups from the database
    """

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

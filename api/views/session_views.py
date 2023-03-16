from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import SessionSerializers


class SessionList(generics.ListAPIView):
    """
    SessionList lists all Session entities
    """

    serializer_class = SessionSerializers
    queryset = Session.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class SessionRetrieve(generics.RetrieveAPIView):
    """
    SessionRetrieve is used to retrieve individual sessions from the database
    """

    serializer_class = SessionSerializers
    queryset = Session.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

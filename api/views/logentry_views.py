from django.contrib.admin.models import LogEntry
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import LogEntrySerializers


class LogEntryList(generics.ListAPIView):
    """
    LogEntryList lists all LogEntry entities
    """

    serializer_class = LogEntrySerializers
    queryset = LogEntry.objects.all()
    # permission_classes = (IsAuthenticated, IsSuperUser)


class LogEntryRetrieve(generics.RetrieveAPIView):
    """
    LogEntryRetrieve is used to retrieve individual logentries from the database
    """

    serializer_class = LogEntrySerializers
    queryset = LogEntry.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

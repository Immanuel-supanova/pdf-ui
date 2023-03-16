from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from myadmin.models import Profile
from ..serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    ProfileList lists all Profile entities
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)


class ProfileRetrieve(generics.RetrieveAPIView):
    """
    ProfileRetrieve is used to retrieve individual profiles from the database
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

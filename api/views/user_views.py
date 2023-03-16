from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsSuperUser
from ..serializers import UserSerializer

User = get_user_model()


class UserList(generics.ListAPIView):
    """
    UserList lists all User entities
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class UserRetrieve(generics.RetrieveAPIView):
    """
    UserRetrieve is used to retrieve individual users from the database
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)

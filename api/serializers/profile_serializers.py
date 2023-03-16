from rest_framework import serializers

from myadmin.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """This is a serializer for Profile Model"""
    username = serializers.SerializerMethodField("get_username")
    first_name = serializers.SerializerMethodField("get_first_name")
    last_name = serializers.SerializerMethodField("get_last_name")
    date_joined = serializers.SerializerMethodField("get_date_created")

    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'user', 'profile_img', 'bio', 'date_joined']

    def get_username(self, profile):
        username = profile.user.username
        return username

    def get_first_name(self, profile):
        first_name = profile.user.first_name
        return first_name

    def get_last_name(self, profile):
        last_name = profile.user.last_name
        return last_name

    def get_date_created(self, profile):
        date = profile.user.date_joined
        return date

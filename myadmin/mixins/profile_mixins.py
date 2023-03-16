from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType


# Mixins for Profile model
class ProfileUpdateMixin(UserPassesTestMixin):
    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.user.username,
            action_flag=CHANGE)
        return response

    def test_func(self):
        return self.request.user.has_perm('change_profile')


class ProfileViewMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_perm('view_profile')

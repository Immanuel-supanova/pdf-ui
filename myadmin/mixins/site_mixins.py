from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


# Mixins for Sites model
class SiteCreateMixin(UserPassesTestMixin):

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.domain,
            action_flag=ADDITION)
        return response

    def test_func(self):
        return self.request.user.has_perm('add_site')


class SiteUpdateMixin(UserPassesTestMixin):

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.domain,
            action_flag=CHANGE)
        return response

    def test_func(self):
        return self.request.user.has_perm('change_site')


class SiteDeleteMixin(UserPassesTestMixin):

    def form_valid(self, form):
        success_url = self.get_success_url()
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=self.object.domain,
            action_flag=DELETION)
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        return self.request.user.has_perm('delete_site')


class SiteViewMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_perm('view_site')

# Mixins for FlatPage model
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


class FlatPageCreateMixin(UserPassesTestMixin):

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.title,
            action_flag=ADDITION)
        return response

    def test_func(self):
        return self.request.user.has_perm('add_flatpage')


class FlatPageUpdateMixin(UserPassesTestMixin):

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.title,
            action_flag=CHANGE)
        return response

    def test_func(self):
        return self.request.user.has_perm('change_flatpage')


class FlatPageDeleteMixin(UserPassesTestMixin):

    def form_valid(self, form):
        success_url = self.get_success_url()
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=self.object.title,
            action_flag=DELETION)
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        return self.request.user.has_perm('delete_flatpage')


class FlatPageViewMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_perm('view_flatpage')

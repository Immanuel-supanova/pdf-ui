from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .flatpage_mixins import FlatPageCreateMixin, FlatPageUpdateMixin, FlatPageDeleteMixin, FlatPageViewMixin
from .group_mixins import GroupCreateMixin, GroupUpdateMixin, GroupDeleteMixin, GroupViewMixin
from .profile_mixins import ProfileUpdateMixin, ProfileViewMixin
from .redirect_mixins import RedirectCreateMixin, RedirectUpdateMixin, RedirectDeleteMixin, RedirectViewMixin
from .site_mixins import SiteCreateMixin, SiteUpdateMixin, SiteDeleteMixin, SiteViewMixin
from .user_mixins import UserCreateMixin, UserUpdateMixin, UserDeleteMixin, UserViewMixin


class MyadminMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_superuser

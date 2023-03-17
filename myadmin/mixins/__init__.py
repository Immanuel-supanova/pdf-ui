from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.flatpages.models import FlatPage
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.db.models import Q
from django.shortcuts import render

from .flatpage_mixins import FlatPageCreateMixin, FlatPageUpdateMixin, FlatPageDeleteMixin, FlatPageViewMixin
from .group_mixins import GroupCreateMixin, GroupUpdateMixin, GroupDeleteMixin, GroupViewMixin
from .profile_mixins import ProfileUpdateMixin, ProfileViewMixin
from .redirect_mixins import RedirectCreateMixin, RedirectUpdateMixin, RedirectDeleteMixin, RedirectViewMixin
from .site_mixins import SiteCreateMixin, SiteUpdateMixin, SiteDeleteMixin, SiteViewMixin
from .user_mixins import UserCreateMixin, UserUpdateMixin, UserDeleteMixin, UserViewMixin

User = get_user_model()


class MyadminMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_superuser


class SearchMixin:
    def post(self, request, **kwargs):
        searched = self.request.POST['searched']
        users = User.objects.filter(Q(username__icontains=searched) |
                                    Q(first_name__icontains=searched) |
                                    Q(last_name__icontains=searched))
        groups = Group.objects.filter(Q(name__icontains=searched))
        flatpages = FlatPage.objects.filter(Q(url__icontains=searched) | Q(title__icontains=searched))
        redirects = Redirect.objects.filter(Q(old_path__contains=searched) | Q(new_path__icontains=searched))
        sites = Site.objects.filter(Q(domain__icontains=searched) | Q(name__icontains=searched))

        return render(request,
                      'myadmin/index.html',
                      {'searched': searched,
                       'users': users,
                       'groups': groups,
                       'flatpages': flatpages,
                       'redirects': redirects,
                       'sites': sites,
                       }
                      )

import datetime

from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

from .flatpage_views import FlatPageCreateView, FlatPageUpdateView, FlatPageDeleteView, FlatPageListView, \
    FlatPageDetailView
from .group_views import GroupCreateView, GroupUpdateView, GroupDeleteView, GroupListView, GroupDetailView
from .profile_views import ProfileUpdateView, ProfileDetailView
from .redirect_views import RedirectCreateView, RedirectUpdateView, RedirectDeleteView, RedirectListView, \
    RedirectDetailView
from .site_views import SiteCreateView, SiteUpdateView, SiteDeleteView, SiteListView, SiteDetailView
from .user_views import UserListView, UserUpdateView, UserCreateView, UserDeleteView, UserDetailView
from ..mixins import MyadminMixin, SearchMixin

User = get_user_model()

current_day = datetime.datetime.now().day
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year


# Create your views here.
class HomePage(MyadminMixin, SearchMixin, TemplateView):
    template_name = "myadmin/index.html"

    def get_context_data(self, **kwargs):
        # ___________________________________________________________
        context = super().get_context_data(**kwargs)

        context['current_day'] = current_day
        context['current_month'] = current_month
        context['current_year'] = current_year

        context['logentry_day'] = LogEntry.objects.filter(action_time__day=current_day).count()
        context['logentry_month'] = LogEntry.objects.filter(action_time__month=current_month).count()
        context['logentry_year'] = LogEntry.objects.filter(action_time__year=current_year).count()

        context['logentry'] = LogEntry.objects.all()

        return context

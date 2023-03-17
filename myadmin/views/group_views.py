from django.contrib.auth.models import Group
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from myadmin.forms.group_forms import GroupForm
from myadmin.mixins import MyadminMixin, GroupCreateMixin, GroupUpdateMixin, GroupViewMixin, GroupDeleteMixin, \
    SearchMixin


class GroupCreateView(MyadminMixin, SearchMixin, GroupCreateMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'myadmin/group/group_create.html'

    def get_success_url(self):
        return reverse('myadmin-group-list')


class GroupUpdateView(MyadminMixin, SearchMixin, GroupUpdateMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'myadmin/group/group_update.html'

    def get_success_url(self):
        return reverse('myadmin-group-list')


class GroupDeleteView(MyadminMixin, SearchMixin, GroupDeleteMixin, DeleteView):
    model = Group
    template_name = 'myadmin/group/group_delete.html'

    def get_success_url(self):
        return reverse('myadmin-group-list')


class GroupListView(MyadminMixin, SearchMixin, GroupViewMixin, ListView):
    model = Group
    template_name = 'myadmin/group/group_list.html'


class GroupDetailView(MyadminMixin, SearchMixin, GroupViewMixin, DetailView):
    model = Group
    template_name = 'myadmin/group/group_detail.html'

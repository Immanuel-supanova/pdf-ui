from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from ..forms import UserUpdateForm, UserCreateForm
from ..mixins import MyadminMixin, UserCreateMixin, UserUpdateMixin, UserDeleteMixin, UserViewMixin, SearchMixin
from ..models import Profile

User = get_user_model()


class UserListView(MyadminMixin, SearchMixin, UserViewMixin, ListView):
    model = User
    template_name = 'myadmin/user/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field = ['#', 'username', 'firstname', 'lastname', 'email', 'active', 'Last Login']
        context['field'] = field

        return context


class UserDetailView(MyadminMixin, SearchMixin, UserViewMixin, DetailView):
    model = User
    template_name = 'myadmin/user/user_detail.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)
        logentry = LogEntry.objects.filter(user=self.object.id)
        paginator = Paginator(logentry, 10)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        profile = Profile.objects.get(user=self.object.id)

        context['permissions'] = Permission.objects.count()
        context['page_obj'] = page_obj
        context['profile'] = profile

        return context


class UserCreateView(MyadminMixin, SearchMixin, UserCreateMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'myadmin/user/user_create.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse('myadmin-user-list')


class UserUpdateView(MyadminMixin, SearchMixin, UserUpdateMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'myadmin/user/user_change.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse('myadmin-user-list')


class UserDeleteView(MyadminMixin, SearchMixin, UserDeleteMixin, DeleteView):
    model = User
    template_name = 'myadmin/user/user_delete.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse('myadmin-user-list')

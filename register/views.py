from django.contrib.admin.models import LogEntry, CHANGE, DELETION
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import RegisterForm, UserChangeForm

User = get_user_model()


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "auth/signup.html"

    def get_success_url(self, *args, **kwargs):  # use this to direct to its immediate detail view
        return reverse_lazy('home')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'auth/user_change.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = User.objects.get(id=self.request.user.id)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=self.object.username,
            action_flag=CHANGE)
        profile.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse('home')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'auth/user_delete.html'
    model = User

    def form_valid(self, form):
        success_url = self.get_success_url()
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=self.object.username,
            action_flag=DELETION)
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse('home')


def bad_request_view(request, exception):
    return render(request, '400.html', status=400)


def access_denied_view(request, exception):
    return render(request, '403.html', status=403)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def internal_server_view(request):
    return render(request, '500.html', status=500)

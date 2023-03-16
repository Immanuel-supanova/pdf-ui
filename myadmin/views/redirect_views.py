from django.contrib.redirects.models import Redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from ..forms import RedirectForm
from ..mixins import MyadminMixin, RedirectCreateMixin, RedirectUpdateMixin, RedirectDeleteMixin, RedirectViewMixin


class RedirectCreateView(MyadminMixin, RedirectCreateMixin, CreateView):
    model = Redirect
    form_class = RedirectForm
    template_name = 'myadmin/redirect/redirect_create.html'

    def get_success_url(self):
        return reverse('myadmin-redirect-list')


class RedirectUpdateView(MyadminMixin, RedirectUpdateMixin, UpdateView):
    model = Redirect
    form_class = RedirectForm
    template_name = 'myadmin/redirect/redirect_update.html'

    def get_success_url(self):
        return reverse('myadmin-redirect-list')


class RedirectDeleteView(MyadminMixin, RedirectDeleteMixin, DeleteView):
    model = Redirect
    template_name = 'myadmin/redirect/redirect_delete.html'

    def get_success_url(self):
        return reverse('myadmin-redirect-list')


class RedirectListView(MyadminMixin, RedirectViewMixin, ListView):
    model = Redirect
    template_name = 'myadmin/redirect/redirect_list.html'


class RedirectDetailView(MyadminMixin, RedirectViewMixin, DetailView):
    model = Redirect
    template_name = 'myadmin/redirect/redirect_detail.html'

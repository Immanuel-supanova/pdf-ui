from django.contrib.sites.models import Site
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from ..forms import SiteForm
from ..mixins import MyadminMixin, SiteCreateMixin, SiteUpdateMixin, SiteDeleteMixin, SiteViewMixin


class SiteCreateView(MyadminMixin, SiteCreateMixin, CreateView):
    model = Site
    form_class = SiteForm
    template_name = 'myadmin/site/site_create.html'

    def get_success_url(self):
        return reverse('myadmin-site-list')


class SiteUpdateView(MyadminMixin, SiteUpdateMixin, UpdateView):
    model = Site
    form_class = SiteForm
    template_name = 'myadmin/site/site_update.html'

    def get_success_url(self):
        return reverse('myadmin-site-list')


class SiteDeleteView(MyadminMixin, SiteDeleteMixin, DeleteView):
    model = Site
    template_name = 'myadmin/site/site_delete.html'

    def get_success_url(self):
        return reverse('myadmin-site-list')


class SiteListView(MyadminMixin, SiteViewMixin, ListView):
    model = Site
    template_name = 'myadmin/site/site_list.html'


class SiteDetailView(MyadminMixin, SiteViewMixin, DetailView):
    model = Site
    template_name = 'myadmin/site/site_detail.html'

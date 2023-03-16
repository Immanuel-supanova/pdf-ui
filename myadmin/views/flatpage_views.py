from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from ..forms import FlatPageForm
from ..mixins import MyadminMixin, FlatPageViewMixin, FlatPageDeleteMixin, FlatPageUpdateMixin, FlatPageCreateMixin


class FlatPageCreateView(MyadminMixin, FlatPageCreateMixin, CreateView):
    model = FlatPage
    form_class = FlatPageForm
    template_name = 'myadmin/flatpage/flatpage_create.html'

    def get_success_url(self):
        return reverse('myadmin-flatpage-list')


class FlatPageUpdateView(MyadminMixin, FlatPageUpdateMixin, UpdateView):
    model = FlatPage
    form_class = FlatPageForm
    template_name = 'myadmin/flatpage/flatpage_update.html'

    def get_success_url(self):
        return reverse('myadmin-flatpage-list')


class FlatPageDeleteView(MyadminMixin, FlatPageDeleteMixin, DeleteView):
    model = FlatPage
    form_class = FlatPageForm
    template_name = 'myadmin/flatpage/flatpage_delete.html'

    def get_success_url(self):
        return reverse('myadmin-flatpage-list')


class FlatPageListView(MyadminMixin, FlatPageViewMixin, ListView):
    model = FlatPage
    template_name = 'myadmin/flatpage/flatpage_list.html'


class FlatPageDetailView(MyadminMixin, FlatPageViewMixin, DetailView):
    model = FlatPage
    template_name = 'myadmin/flatpage/flatpage_detail.html'

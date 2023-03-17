from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import UpdateView, DetailView

from ..forms import ProfileForm
from ..mixins import MyadminMixin, ProfileUpdateMixin, ProfileViewMixin, SearchMixin
from ..models import Profile

User = get_user_model()


# Create your views here.

class ProfileUpdateView(MyadminMixin, SearchMixin, ProfileUpdateMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'myadmin/profile_change.html'

    def get_success_url(self):
        return reverse('myadmin-user-list')


class ProfileDetailView(MyadminMixin, SearchMixin, ProfileViewMixin, DetailView):
    model = Profile
    template_name = 'myadmin/profile.html'

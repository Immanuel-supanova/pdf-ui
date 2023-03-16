from django.urls import path, include

from . import profile_urls, user_urls, group_urls, flatpage_urls, redirect_urls, site_urls
from ..views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="myadmin"),
    path('profile/', include(profile_urls)),
    path('user/', include(user_urls)),
    path('group/', include(group_urls)),
    path('flatpage/', include(flatpage_urls)),
    path('redirect/', include(redirect_urls)),
    path('site/', include(site_urls)),
]

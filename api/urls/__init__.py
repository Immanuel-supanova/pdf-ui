from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import users_urls, group_urls, contenttype_urls, flatpage_urls, logentry_urls, permissions_urls, redirect_urls, \
    session_urls, profile_urls

urlpatterns = [
    path('users/', include(users_urls)),
    path('groups/', include(group_urls)),
    path('token/', obtain_auth_token),
    path('contenttype/', include(contenttype_urls)),
    path('flatpage/', include(flatpage_urls)),
    path('logentry/', include(logentry_urls)),
    path('permissions/', include(permissions_urls)),
    path('redirect/', include(redirect_urls)),
    path('session/', include(session_urls)),
    path('profile/', include(profile_urls))
]

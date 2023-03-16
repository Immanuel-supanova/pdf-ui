from django.urls import path

from myadmin.views import ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('change/<int:pk>/', ProfileUpdateView.as_view(), name='profile_change'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
]

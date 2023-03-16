from django.urls import path

from myadmin.views import SiteCreateView, SiteUpdateView, SiteDeleteView, SiteListView, SiteDetailView

urlpatterns = [
    path('create/', SiteCreateView.as_view(), name='myadmin-site-create'),
    path('change/<int:pk>/', SiteUpdateView.as_view(), name='myadmin-site-update'),
    path('delete/<int:pk>/', SiteDeleteView.as_view(), name='myadmin-site-delete'),
    path('list/', SiteListView.as_view(), name='myadmin-site-list'),
    path('<int:pk>/', SiteDetailView.as_view(), name='myadmin-site-detail'),

]

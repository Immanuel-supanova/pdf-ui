from django.urls import path

from myadmin.views import RedirectCreateView, RedirectUpdateView, RedirectDeleteView, RedirectListView, \
    RedirectDetailView

urlpatterns = [
    path('create/', RedirectCreateView.as_view(), name='myadmin-redirect-create'),
    path('change/<int:pk>/', RedirectUpdateView.as_view(), name='myadmin-redirect-update'),
    path('delete/<int:pk>/', RedirectDeleteView.as_view(), name='myadmin-redirect-delete'),
    path('list/', RedirectListView.as_view(), name='myadmin-redirect-list'),
    path('<int:pk>/', RedirectDetailView.as_view(), name='myadmin-redirect-detail'),

]

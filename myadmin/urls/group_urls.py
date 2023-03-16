from django.urls import path

from myadmin.views import GroupCreateView, GroupUpdateView, GroupDeleteView, GroupListView, GroupDetailView

urlpatterns = [
    path('create/', GroupCreateView.as_view(), name='myadmin-group-create'),
    path('change/<int:pk>/', GroupUpdateView.as_view(), name='myadmin-group-update'),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='myadmin-group-delete'),
    path('list/', GroupListView.as_view(), name='myadmin-group-list'),
    path('<int:pk>/', GroupDetailView.as_view(), name='myadmin-group-detail'),

]

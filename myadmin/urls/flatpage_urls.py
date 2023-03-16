from django.urls import path

from ..views import FlatPageCreateView, FlatPageUpdateView, FlatPageDeleteView, FlatPageListView, FlatPageDetailView

urlpatterns = [
    path('create/', FlatPageCreateView.as_view(), name='myadmin-flatpage-create'),
    path('change/<int:pk>/', FlatPageUpdateView.as_view(), name='myadmin-flatpage-update'),
    path('delete/<int:pk>/', FlatPageDeleteView.as_view(), name='myadmin-flatpage-delete'),
    path('list/', FlatPageListView.as_view(), name='myadmin-flatpage-list'),
    path('<int:pk>/', FlatPageDetailView.as_view(), name='myadmin-flatpage-detail'),

]

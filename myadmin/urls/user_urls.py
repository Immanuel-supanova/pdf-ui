from django.urls import path

from myadmin.views import UserListView, UserUpdateView, UserCreateView, UserDeleteView, UserDetailView

urlpatterns = [
    path('list/', UserListView.as_view(), name="myadmin-user-list"),
    path('change/<int:pk>/', UserUpdateView.as_view(), name="myadmin-user-update"),
    path('create/', UserCreateView.as_view(), name="myadmin-user-create"),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name="myadmin-user-delete"),
    path('<int:pk>/', UserDetailView.as_view(), name="myadmin-user-detail"),

]

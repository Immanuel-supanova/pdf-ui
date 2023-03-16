from django.urls import path

from ..views import PermissionList, PermissionRetrieve

urlpatterns = [
    path('', PermissionList.as_view()),
    path('<int:pk>/', PermissionRetrieve.as_view())

]

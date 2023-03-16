from django.urls import path

from ..views import UserList, UserRetrieve

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserRetrieve.as_view()),
]

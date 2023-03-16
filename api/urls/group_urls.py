from django.urls import path

from ..views import GroupList, GroupRetrieve

urlpatterns = [
    path('', GroupList.as_view()),
    path('<int:pk>/', GroupRetrieve.as_view())
]

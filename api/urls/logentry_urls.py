from django.urls import path

from ..views import LogEntryList, LogEntryRetrieve

urlpatterns = [
    path('', LogEntryList.as_view()),
    path('<int:pk>/', LogEntryRetrieve.as_view())
]

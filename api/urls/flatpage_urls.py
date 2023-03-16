from django.urls import path

from ..views import FlatPageList, FlatPageRetrieve

urlpatterns = [
    path('', FlatPageList.as_view()),
    path('<int:pk>/', FlatPageRetrieve.as_view())
]

from django.urls import path

from ..views import SessionList, SessionRetrieve

urlpatterns = [
    path('', SessionList.as_view()),
    path('<int:pk>/', SessionRetrieve.as_view())
]

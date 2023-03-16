from django.urls import path

from ..views import ProfileList, ProfileRetrieve

urlpatterns = [
    path('', ProfileList.as_view()),
    path('<int:pk>/', ProfileRetrieve.as_view()),
]

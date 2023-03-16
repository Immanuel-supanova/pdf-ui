from django.urls import path

from ..views import RedirectList, RedirectRetrieve

urlpatterns = [
    path('', RedirectList.as_view()),
    path('<int:pk>/', RedirectRetrieve.as_view())
]

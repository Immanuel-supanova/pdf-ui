from django.urls import path

from ..views import ContentTypeList, ContentTypeRetrieve

urlpatterns = [
    path('', ContentTypeList.as_view()),
    path('<int:pk>/', ContentTypeRetrieve.as_view())
]

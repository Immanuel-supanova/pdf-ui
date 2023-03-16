from django.urls import path

from .views import PdfCreateView, PdfDetailView, PdfUpdateView, pdf_delete_view, download_pdf, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new/', PdfCreateView.as_view(), name='pdf-create'),
    path('<int:pk>/', PdfDetailView.as_view(), name='pdf-detail'),
    path('change/<int:pk>', PdfUpdateView.as_view(), name='pdf-update'),
    path('delete/<int:pk>', pdf_delete_view, name='pdf-delete'),
    path('download/<int:pk>', download_pdf, name='pdf-download')
]

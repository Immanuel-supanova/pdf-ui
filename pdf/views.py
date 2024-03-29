import io

from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import FileResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from xhtml2pdf import pisa

from .forms import DocumentForm
from .mixins import PdfCreateMixin, PdfUpdateMixin, PdfViewMixin
from .models import PdfDocument

# Create your views here.

User = get_user_model()

today = timezone.now()


# Create your views here.

def download_pdf(request, pk):
    # Create Bytestream buffer
    buf = io.BytesIO()

    # Designate The Model
    pdf = PdfDocument.objects.get(id=pk)

    # create pdf
    pisa.CreatePDF(
        pdf.content,
        dest=buf,
    )

    # Finish Up
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename=f'{pdf.title}.pdf')


class PdfCreateView(LoginRequiredMixin, PdfCreateMixin, CreateView):
    template_name = "pdf/create_pdf.html"
    model = PdfDocument
    form_class = DocumentForm

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = User.objects.get(id=self.request.user.id)
        blog.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):  # use this to direct to its immediate detail view
        return reverse_lazy('pdf-detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        context_p = User.objects.all()
        return context_p

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['user'] = User.objects.filter(id=self.request.user.id)

        return context


class PdfUpdateView(LoginRequiredMixin, PdfUpdateMixin, UpdateView):
    template_name = "pdf/update_pdf.html"
    model = PdfDocument
    form_class = DocumentForm

    def form_valid(self, form):
        txt = form.save(commit=False)
        txt.date_modified = today
        txt.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):  # use this to direct to its immediate detail view
        return reverse_lazy('pdf-detail', kwargs={'pk': self.object.pk})


def pdf_delete_view(request, pk):
    pdf = PdfDocument.objects.get(id=pk)
    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(PdfDocument).pk,
        object_id=pdf.id,
        object_repr=pdf.title,
        action_flag=DELETION)
    pdf.delete()
    return redirect('home')


class PdfDetailView(LoginRequiredMixin, PdfViewMixin, DetailView):
    template_name = "pdf/detail_pdf.html"
    model = PdfDocument


class HomeView(TemplateView):
    template_name = "pdf/home.html"

    def get_queryset(self):
        context_p = User.objects.all()
        return context_p

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        user = User.objects.filter(id=self.request.user.id)
        context['user'] = user
        context['document'] = PdfDocument.objects.filter(author=self.request.user.id)

        return context

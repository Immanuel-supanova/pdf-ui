# Create your models here.

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


# Create your models here.
class PdfDocument(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextField(config_name='default')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def name(self):
        return f'{self.title}.pdf'

    def __str__(self):
        return self.name()

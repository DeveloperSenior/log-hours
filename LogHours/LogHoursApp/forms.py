from django import forms
from LogHoursApp.models import LogHours
from django.contrib.admin.widgets import AdminDateWidget

from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label="Archivo",
                           validators=[FileExtensionValidator(allowed_extensions=["xls", "xlsx"])])


class LogHoursForm(forms.ModelForm):
    date = forms.DateTimeField(required=True, widget=AdminDateWidget)

    class Meta:
        model = LogHours
        exclude = ()

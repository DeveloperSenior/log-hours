from django import forms
from LogHoursApp.models import LogHours
from django.contrib.admin.widgets import AdminDateWidget

from django.core.validators import FileExtensionValidator


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label="Archivo",
                           validators=[FileExtensionValidator(allowed_extensions=["xls", "xlsx"])])


class LogHoursForm(forms.ModelForm):
    date = forms.DateTimeField(required=True, widget=DateInput(attrs={'class': 'vTextField'}))

    class Meta:
        model = LogHours
        exclude = ()

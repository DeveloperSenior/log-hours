from django import forms
from LogHoursApp.models import LogHours


class LogHoursForm(forms.ModelForm):
    class Meta:
        model = LogHours
        fields = "__all__"

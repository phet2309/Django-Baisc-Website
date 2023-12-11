# Author: Het Patel

from django import forms
from hello.models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message", "name", "cname")   # NOTE: the trailing comma is required

from django import forms
from django_summernote.fields import SummernoteWidget


class SummerFieldForm(forms.Form):
    text = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
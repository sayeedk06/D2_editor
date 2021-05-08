from .models import TextData
from django import forms
class TextDataForm(forms.ModelForm):
    class Meta:
        model = TextData
        fields = ('text', 'text_url_id')
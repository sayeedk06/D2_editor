from .models import TextData,TextHist
from django import forms
class TextDataForm(forms.ModelForm):
    class Meta:
        model = TextData
        fields = ('text', 'text_url_id')
class TextHisForm(forms.ModelForm):
    class Meta:
        model = TextHist
        fields = '__all__'
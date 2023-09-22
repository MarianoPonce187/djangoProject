from django import forms
from .models import Palabra

class PalabraForm(forms.ModelForm):
    class Meta:
        model = Palabra
        fields = ['palabra']

    def clean_palabra(self):
        palabra = self.cleaned_data['palabra']
        if palabra == palabra[::-1]:
            self.instance.es_palindromo = True
        return palabra
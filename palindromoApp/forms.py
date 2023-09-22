from django import forms
from .models import Palindromo

class PalabraForm(forms.ModelForm):
    class Meta:
        model = Palindromo
        fields = ['palabra']

    def clean_palabra(self):
        palabra = self.cleaned_data['palabra']
        if palabra == palabra[::-1]:
            self.instance.es_palindromo = True
        return palabra
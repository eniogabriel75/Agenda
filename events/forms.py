from django.db.models import fields
from django import forms
from .models import Eventos


class Date(forms.DateInput):
    input_type = 'date'

class AddEvent(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = "__all__"
        widgets = {'registrationDate': Date()}

    def __init__(self, *args, **kwargs):
        #herdando metódo da classe e sobrescrevendo apenas
        #metódo que nos interessa
        super().__init__(*args, **kwargs)
        #transformando usuário em um 'Hiddeninput'
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['tipo'].widget = forms.HiddenInput()
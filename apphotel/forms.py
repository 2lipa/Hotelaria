from django import forms
from .models import Local, Locador, Reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_entrada', 'data_saida']
        widgets = {
            "entrada": DateInput(),
            "saida": DateInput()
        }

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['locador','nome_local', 'propriedade', 'preco', 'nota_avaliacao', 'wifi', 'tv' , 'camas', 'descricao']

class LocadorForm(forms.ModelForm):
    class Meta:
        model = Locador
        fields = ['nome', 'pais', 'cidade', 'bairro']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'pais': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
        }
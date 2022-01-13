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
        widgets = {
            'locador': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'nome_local': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'propriedade': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'preco': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'nota_avaliacao': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'wifi': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'tv': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'camas': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control mb-3 mt-4'}),
        }

class LocadorForm(forms.ModelForm):
    class Meta:
        model = Locador
        fields = ['nome', 'pais', 'cidade', 'rua']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'pais': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
            'rua': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1'}),
        }
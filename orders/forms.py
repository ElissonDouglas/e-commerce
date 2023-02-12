from django import forms
from django.contrib.auth.models import User
from .models import Order

class PagamentoForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('nome', 'email', 'endereco', 'cidade', 'estado', 'cep')


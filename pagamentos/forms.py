from django import forms
from django.contrib.auth.models import User
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    
    class Meta:
        model = Pagamento
        fields = ('nome', 'email', 'endereco', 'cidade', 'estado', 'cep')


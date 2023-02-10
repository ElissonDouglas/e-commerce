from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome', 'email', 'endereco', 'cidade', 'estado', 'cep')

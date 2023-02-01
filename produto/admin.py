from django.contrib import admin
from .models import CategoriaProduto, Produto

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criado', 'modificado',)
    
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'preco', 'categoria', 'descricao', 'ativo', 'criado', 'modificado',)
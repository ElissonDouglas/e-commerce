from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Produto, CategoriaProduto


def produtoview(request, pk):
    prod = get_object_or_404(Produto, id=pk)
    prod_filtrado = Produto.objects.filter(categoria=prod.categoria).exclude(id=prod.id)
    
    context = {
        'produto': prod,
        'produtos_filtrado': prod_filtrado,
    }
    
    return render(request, 'produto.html', context)


class SearchView(TemplateView):
    template_name = 'search.html'
    
    
    def get(self, request, *args, **kwargs):
        pesquisa = request.GET.get('search-bar', '').strip()
        
        produtos_pesquisa = Produto.objects.filter(nome__icontains=pesquisa)
        if len(produtos_pesquisa) == 0:
            print('Sem produtos')
        
        context = {
            'pesquisa': pesquisa,
            'produtos_pesquisa': produtos_pesquisa
        }

        return render(request, 'search.html', context)
    

def categoriaview(request, pk):
    categoria = get_object_or_404(CategoriaProduto, id=pk)
    produtos_categoria = Produto.objects.filter(categoria=categoria.id)
    
    return render(request, 'categoria.html', {'produtos': produtos_categoria, 'categoria': categoria,})
    
    
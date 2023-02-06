from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, CategoriaProduto, Carrinho, ItemCarrinho
from django.contrib.auth.models import User


from decimal import Decimal

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
        
        
        
        context = {
            'pesquisa': pesquisa,
            'produtos_pesquisa': produtos_pesquisa
        }

        return render(request, 'search.html', context)
    

def categoriaview(request, pk):
    categoria = get_object_or_404(CategoriaProduto, id=pk)
    produtos_categoria = Produto.objects.filter(categoria=categoria.id)
    
    return render(request, 'categoria.html', {'produtos': produtos_categoria, 'categoria': categoria,})


@login_required
def carrinhoview(request):
    if request.method == 'POST':
        user = request.user
        produto = int(request.POST.get('produto_carrinho'))
        quantidade = int(request.POST.get('quantidade'))
        preco = Decimal(request.POST.get('produto_preco').replace(',', '.'))
        total = Decimal(float(preco)) * quantidade
        
        print(produto)
        
        try:
            item = ItemCarrinho.objects.get(produto=produto)
            return redirect('carrinho')
        except ItemCarrinho.DoesNotExist:
            # Criando carrinho/Acessando carrinho existente e adicionando o produto.
            carrinho, created = Carrinho.objects.get_or_create(usuario=user)
        
            carrinho.adicionar_produto(produto=produto, quantidade=quantidade, preco=preco, total=Decimal(total))
            
            # Redirecionando o usuário para o carrinho.
            return redirect('carrinho')  
    else:
        try:
            user = User.objects.get(username=request.user)
            carrinho = Carrinho.objects.get(usuario_id=user.id)
            produtos_carrinho = ItemCarrinho.objects.filter(carrinho_id=carrinho.id)
            aux = []
            for produto in produtos_carrinho:
                prod = Produto.objects.get(id=produto.produto)
                aux.append({'produto': prod, 'quantidade': produto.quantidade})
                
            context = {
            'carrinho': carrinho,
            'produtos_carrinho': aux,
            }
            return render(request, 'carrinho.html', context)
            
        except Carrinho.DoesNotExist:
            Carrinho.objects.create(usuario=request.user)
        
        # Recuperando os produtos que estão dentro do carrinho do usuário
        
            
        
        return render(request, 'carrinho.html')
            
        
    
  
def deleteitem(request, produto_id):
    item_carrinho = ItemCarrinho.objects.get(produto=produto_id)
    carrinho = Carrinho.objects.get(id=item_carrinho.carrinho_id)
    carrinho.total -= item_carrinho.preco * item_carrinho.quantidade
    carrinho.save()
    item_carrinho.delete()
    return redirect('carrinho')
  
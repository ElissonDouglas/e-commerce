from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from produto.models import Produto, Carrinho, ItemCarrinho
from .models import Order
from .forms import PagamentoForm


@login_required
def order(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        user = request.user
        
        if form.is_valid():
            carrinho = Carrinho.objects.get(usuario=request.user)
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            endereco = form.cleaned_data['endereco']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            cep = form.cleaned_data['cep']
            
            new_order = Order(carrinho=carrinho, nome=nome, email=email, endereco=endereco, cidade=cidade, estado=estado, cep=cep)
            new_order.save()
            
            for i in itens:
                produto = Produto.objects.get(id=i.produto)
                quantidade = i.quantidade
                preco = i.preco
                new_order.get_order_items(produto=produto, quantidade=quantidade, order=new_order, preco=preco, total=quantidade*preco)
            messages.success(request, 'Pedido realizado com sucesso!')
            
            return render(request, 'order.html')
    else:
        all_products = []
        for item in itens:
            produto = Produto.objects.get(id=item.produto)
            if item.quantidade > 0:
                all_products.append({'produto': produto, 'quantidade': item.quantidade})
        
        context = {
            'total': carrinho.total,
            'produtos': all_products,
            'form': PagamentoForm()
        }
        
        return render(request, 'order.html', context)

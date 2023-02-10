from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from produto.models import Produto, Carrinho, ItemCarrinho
from .models import Pagamento
from .forms import PagamentoForm


@login_required
def order(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        
        if form.is_valid():
            usuario = request.user
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            endereco = form.cleaned_data['endereco']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            cep = form.cleaned_data['cep']
            
            new_order = Pagamento(usuario=usuario, nome=nome, email=email, endereco=endereco, cidade=cidade, estado=estado, cep=cep)
            new_order.save()
            
            return render(request, 'order.html')
    else:
        carrinho = Carrinho.objects.get(usuario=request.user)
        itens = ItemCarrinho.objects.filter(carrinho=carrinho)
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

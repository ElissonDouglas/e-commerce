from django.db import models
from produto.models import Carrinho, Produto

from decimal import Decimal

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    finalizado = models.BooleanField('Finalizado', default=False)

    class Meta:
        abstract = True
        

class Order(Base):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, default=None)
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email', max_length=100)
    endereco = models.CharField('Endereço', max_length=250)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cep = models.CharField('Cep', max_length=9)
    total = total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=Decimal(0.00))
    
    
    def get_order_items(self, produto, quantidade, order, preco, total):
        item = OrderItems.objects.create(produto=produto, quantidade=quantidade, order=order, preco=preco)
        
        self.total += Decimal(total)
        self.save()
    
    
    def __str__(self) -> str:
        return str(self.id)
    

class OrderItems(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=Decimal(0.00))
    

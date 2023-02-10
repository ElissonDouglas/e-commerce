from django.db import models
from django.contrib.auth.models import User
from produto.models import Carrinho


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    finalizado = models.BooleanField('Ativo', default=False)

    class Meta:
        abstract = True
        

class Pagamento(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email', max_length=100)
    endereco = models.CharField('Endereço', max_length=250)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cep = models.CharField('Cep', max_length=9)
    
    
    def __str__(self) -> str:
        return f'Usuário: {self.usuario.username}\nEmail: {self.email}'
    
    
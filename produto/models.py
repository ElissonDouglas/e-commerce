from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField
import uuid
from decimal import Decimal


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class CategoriaProduto(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.nome


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    descricao = models.TextField('Descrição', max_length=400, blank=True)
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE)
    estoque = models.IntegerField('Qntd.', default=0)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={
                           'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return self.nome


class Carrinho(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=Decimal(0.00))

    def adicionar_produto(self, produto, quantidade, preco, total):
        item = ItemCarrinho.objects.create(carrinho=self, produto=produto, quantidade=quantidade, preco=preco)
        self.total += total

        self.save()


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.IntegerField('produto_id', db_index=True)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

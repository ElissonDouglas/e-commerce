from django.test import TestCase, Client
from produto.models import get_file_path, Produto, CategoriaProduto, Carrinho, ItemCarrinho
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from decimal import Decimal



class TestGetFilePath(TestCase):
    

    def setUp(self):
        self.filename = 'imagem.png'
    
    
    def test_get_file_path(self):
        titulo = get_file_path(_instance=None, filename=self.filename)
        
        self.assertEqual(str, type(titulo))
        
        
class TestCategoriaProduto(TestCase):
    
    def test_str(self):
        categoria = CategoriaProduto.objects.create(nome='Categoria1', descricao='Categoria1')
        
        self.assertEqual(str(categoria), 'Categoria1')
        
        
class TestProduto(TestCase):
    
    def setUp(self):
        self.categoria = CategoriaProduto.objects.create(nome='Categoria2', descricao='Categoria2')
        
    def test_produto_str(self):
        produto = Produto.objects.create(nome='produto1', descricao='produto1', preco=299, categoria=self.categoria, estoque=10, imagem='jijiaoij.jpg')
        
        self.assertEqual(str(produto), 'produto1')
        
        
class TestCarrinho(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testcarrinho', password='passwordtest')

        self.categoria = CategoriaProduto.objects.create(nome='Categoria3', descricao='Categoria3')
        
        self.produto = Produto.objects.create(nome='produto2', descricao='produto2', preco=299, categoria=self.categoria, estoque=10, imagem='jijigaoij.jpg')
        
    def test_adicionar_produto(self):
        carrinho = Carrinho.objects.create(usuario=self.user)
        
        carrinho.adicionar_produto(produto=self.produto.id, quantidade=1, preco=self.produto.preco, total=Decimal(self.produto.preco * 1))
        
        carrinho_test = Carrinho.objects.get(id=carrinho.id)
        
        self.assertEqual(carrinho_test.total, Decimal(299))
        
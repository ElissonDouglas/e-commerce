from django.test import TestCase, Client
from produto.views import produtoview, SearchView, categoriaview, carrinhoview, deleteitem
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from produto.models import Produto, CategoriaProduto, Carrinho, ItemCarrinho
from decimal import Decimal


class TestProdutoView(TestCase):
    
    def setUp(self):
        self.client = Client()

        self.categoria = CategoriaProduto.objects.create(nome='Categoria4', descricao='Categoria4')
        
        self.produto = Produto.objects.create(nome='produto3', descricao='produto3', preco=299, categoria=self.categoria, estoque=10, imagem='jijigaoij.jpg')
        
    
    def test_categoria_view(self):
        response = self.client.get('/produto/' + str(self.produto.id))
        context = response.context
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('produto', context)
        self.assertIn('produtos_filtrado', context)
        
        
class TestSearchView(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_get(self):
        response = self.client.get(reverse_lazy('search'), {'search-bar': 'notebook'})
        
        context = response.context
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('produtos_pesquisa', context)
        self.assertIn('pesquisa', context)


class TestCategoriaView(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.categoria = CategoriaProduto.objects.create(nome='Categoria4', descricao='Categoria4')
        
        self.produto = Produto.objects.create(nome='produto3', descricao='produto3', preco=299, categoria=self.categoria, estoque=10, imagem='jijigaoij.jpg')
        
    def test_produto_view(self):
        response = self.client.get('/categoria/' + str(self.categoria.id))
        
        context = response.context
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('produtos', context)
        self.assertIn('categoria', context)
        self.assertTemplateUsed('categoria.html')
        
        
class TestCarrinhoView(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testcarrinho', password='testpassword')
        
        self.client = Client()
        self.client.force_login(self.user)
        
        self.categoria = CategoriaProduto.objects.create(nome='Categoria4', descricao='Categoria4')
        
        self.produto = Produto.objects.create(nome='produto3', descricao='produto3', preco=299, categoria=self.categoria, estoque=10, imagem='jijigaoij.jpg')
        
    def test_post(self):
        response_post = self.client.post(reverse_lazy('carrinho'), {
            'produto_carrinho': self.produto.id,
            'quantidade': 1,
            'produto_preco': Decimal(299),
        })
        
        self.assertEqual(response_post.status_code, 302)
        self.assertTemplateUsed('carrinho.html')
        
        response_post2 = self.client.post(reverse_lazy('carrinho'), {
            'produto_carrinho': self.produto.id,
            'quantidade': 1,
            'produto_preco': Decimal(299),
        })
        
        self.assertEqual(response_post.status_code, 302)
        self.assertTemplateUsed('carrinho.html')
        
    def test_get(self):
        response_get = self.client.get(reverse_lazy('carrinho'))
        context = response_get.context
        
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed('carrinho.html')
        
    def test_get_carrinho(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        
        self.client.get(reverse_lazy('logout'))
        
        self.client.force_login(user)

        carrinho = Carrinho.objects.create(usuario=user)

        produto = Produto.objects.create(nome='test_produto', preco=299, categoria=self.categoria, estoque=10, imagem='aidjioas.png', descricao='kk')

        ItemCarrinho.objects.create(carrinho=carrinho, produto=produto.id, quantidade=1, preco=produto.preco)

        response = self.client.get(reverse_lazy('carrinho'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context)

        
        self.assertEqual(len(response.context['produtos_carrinho']), 1)
        
        self.assertEqual(response.context['produtos_carrinho'][0]['produto'], produto)
        
        self.assertEqual(response.context['produtos_carrinho'][0]['quantidade'], 1)
        
        
class TestDeleteItem(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.categoria = CategoriaProduto.objects.create(nome='categoria114')
        
    def test_delete_item(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        
        self.client.force_login(user)

        carrinho = Carrinho.objects.create(usuario=user)

        produto = Produto.objects.create(nome='test_produto', preco=299, categoria=self.categoria, estoque=10, imagem='aidjioas.png', descricao='kk')

        ItemCarrinho.objects.create(carrinho=carrinho, produto=produto.id, quantidade=1, preco=produto.preco)
        
        response = self.client.get('/deleteitem/' + str(produto.id))
        
        self.assertEqual(response.status_code, 302)
        
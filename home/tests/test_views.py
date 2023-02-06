from django.test import TestCase, Client
from usuarios.views import RegisterForm, CustomLogin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


from django.test import TestCase, Client
from home.views import IndexView
from django.urls import reverse_lazy



class TestIndexView(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    
    def test_index_view(self):
        response = self.client.get(reverse_lazy('index'))
        
        context = response.context
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('informatica', context)
        self.assertIn('eletrodomesticos', context)
        self.assertIn('produtos', context)


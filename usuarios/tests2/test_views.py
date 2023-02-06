from django.test import TestCase, Client
from usuarios.views import RegisterForm, CustomLogin
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class TestRegisterForm(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.client.force_login(self.user)
    
    def test_get_method(self):
        response = self.client.get(reverse_lazy('cadastro'))
        
        self.assertEqual(response.status_code, 302)
        
        self.client.get(reverse_lazy('logout'))
        
        response = self.client.get(reverse_lazy('cadastro'))
        
        self.assertEqual(response.status_code, 200)
        
    def test_form_valid(self):
        self.client.get(reverse_lazy('logout'))
        response = self.client.post(reverse_lazy('cadastro'), {'username': 'testregister', 'password1': 'testpassword', 'password2': 'testpassword'})
        
        self.assertEqual(response.status_code, 302)
        
        
class TestCustomLogin(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser2', password='testpassword')
        
    
    def test_get_success_url(self):
        response = self.client.post(reverse_lazy('login'), {'username': self.user.username, 'password': 'testpassword'})
        
        self.assertEqual(response.status_code, 302)
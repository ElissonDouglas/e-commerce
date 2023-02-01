from django.shortcuts import render
from django.views.generic import TemplateView
from produto.models import Produto, CategoriaProduto





class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['informatica'] = Produto.objects.filter(categoria=1).order_by('?')
        context['produtos'] = Produto.objects.order_by('-id').all()[:5]
        
        return context
    

class ProdutoView(TemplateView):
    template_name = 'produto.html'
    
    
class Error404View(TemplateView):
    template_name = '404.html'
    

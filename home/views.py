from django.shortcuts import render
from django.views.generic import TemplateView
from produto.models import Produto, CategoriaProduto


class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['informatica'] = Produto.objects.filter(categoria=1).order_by('?')[:5]
        context['eletrodomesticos'] = Produto.objects.filter(categoria=2).order_by('?')[:5]
        context['produtos'] = Produto.objects.order_by('-id').all()[:5]
        
        return context
    

class Error404View(TemplateView):
    template_name = '404.html'
    

from django.urls import path
from .views import produtoview, SearchView, categoriaview, carrinhoview, deleteitem, updateitemquantity, updatetotalcart

urlpatterns = [
    path('produto/<int:pk>', produtoview, name='produto'),
    path('get/', SearchView.as_view(), name='search'),
    path('categoria/<int:pk>', categoriaview, name='categoria'),
    path('carrinho/', carrinhoview, name='carrinho'),
    path('deleteitem/<produto_id>', deleteitem, name='deleteitem'),
    path('updateitem/', updateitemquantity, name='updateitem'),
    path('updatetotalcart/', updatetotalcart, name='updatetotalcart'),
]  

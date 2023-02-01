from django.urls import path
from .views import produtoview, SearchView, categoriaview

urlpatterns = [
    path('produto/<int:pk>', produtoview, name='produto'),
    path('get/', SearchView.as_view(), name='search'),
    path('categoria/<int:pk>', categoriaview, name='categoria'),
]

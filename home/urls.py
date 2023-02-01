from .views import IndexView, ProdutoView
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', include('produto.urls'), name='produto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

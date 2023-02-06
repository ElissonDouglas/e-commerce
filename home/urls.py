from .views import IndexView, Error404View
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', include('produto.urls'), name='produto'),
    path('404/', Error404View.as_view(), name='error404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

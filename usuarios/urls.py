from django.urls import path
from .views import register, loginview, logoutview

urlpatterns = [
    path('cadastro/', register, name='cadastro'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
]

from django.urls import path
from .views import CustomLogin, RegisterForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('cadastro/', RegisterForm.as_view(), name='cadastro'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

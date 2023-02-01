from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
            messages.error(request, 'Usuário já está sendo utilizado.')
            return render(request, 'cadastro.html', {})
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name, first_name=first_name)
            
            return redirect('login')
    else:
        return render(request, 'cadastro.html')
    

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
    
def logoutview(request):
    logout(request)
    return redirect('login')
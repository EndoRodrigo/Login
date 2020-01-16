from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('Contenido')
        else:
            return render(request, 'Login.html', {'error': 'Invalid username and password'})

    return render(request, 'Login.html')


def contenido(request):
    return  render(request, 'Contenido.html')

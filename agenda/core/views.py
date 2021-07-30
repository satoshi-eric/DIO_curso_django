from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
# Função para renderizar a página de eventos
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) # Pegando dados do usuario da sessão
    dados = {'eventos': evento} # dicionário a ser passado para o HTML que entende as chaves do dicionário como variáveis
    return render(request, 'agenda.html', dados)

# É possível redirecionar o usuário para outra página com o redirect
# def index(request):
#     return redirect('/agenda')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')
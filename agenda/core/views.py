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

# Redireciona o usuário para a página de login
def login_user(request):
    return render(request, 'login.html')

# Recebe dados de um form pelo usuário através de uma requisição POST
def submit_login(request):
    # Se a requisição for do tipo POST
    if request.POST:
        # Pegando dados do form através do atributo name dos inputs do HTML
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticando usuário
        usuario = authenticate(username=username, password=password)
        # Se a autenticação ocorrer com sucesso, usuario não será None
        if usuario is not None:
            # Cria uma sessão para o usuário
            login(request, usuario)
            return redirect('/')
        else:
            # Mostra uma mensagem de erro na tela onde o usuário está
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')

# Destrói a sessão atual do usuário e atualiza a página
def logout_user(request):
    logout(request)
    return redirect('/')

# Mostra tela de criação de evento 
@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

# Tela com formulário para enviar dados de novo evento
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user

        Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
        
    return redirect('/')
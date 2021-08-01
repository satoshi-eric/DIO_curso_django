from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

@login_required(login_url='/login/')
# Função para renderizar a página de eventos
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual) # Pegando dados do usuario da sessão
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
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

# Tela com formulário para enviar dados de novo evento ou atualizar evento já exeistente
@login_required(login_url='/login/')
def submit_evento(request):
    # Verificando se a requisição veio de um formulário
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            # Evento.objects.filter(id=id_evento).update(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
            # Criando evento para verificar se o usuário que está editando é o mesmo da sessão para que não se possa editar dados de outras pessoas
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
        else:
            Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
        
    return redirect('/')

# Função para deletar eventos pelo id. Recebe um parâmetro pela URl chamado id_evento para identifcar qual evento será excluído
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    # Verifica se o usuário da sessão é o mesmo que está tentando deletar o evento
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo') # Pegando dados do usuario da sessão
    return JsonResponse(list(evento), safe=False)
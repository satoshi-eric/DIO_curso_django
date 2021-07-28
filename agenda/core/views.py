from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.

# Função para renderizar a página de eventos
def lista_eventos(request):
    evento = Evento.objects.all() # pegando todos os eventos do banco de dados
    dados = {'eventos': evento} # dicionário a ser passado para o HTML que entende as chaves do dicionário como variáveis
    return render(request, 'agenda.html', dados)

# É possível redirecionar o usuário para outra página com o redirect
# def index(request):
#     return redirect('/agenda')
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Tabela para agendas

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True) # insere a hora atual quando um valor é inserido no campo
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeira para a models do django User. Se o usuário foi excluído da aplicação, todos os seus eventos também são excluídos

    # Classe de meta dados da classe
    class Meta:
        db_table = 'evento' # ao usarmos o comando sqlmigrate, ele informa que o nome da tabela será core_evento. Para mudar apenas para evento, utilizamos essa propriedade para mudar p nome para evento

    def __str__(self) -> str:
        return self.titulo

    # Método para pegar a data do evento em outro formato
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')
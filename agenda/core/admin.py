from django.contrib import admin
from core.models import Evento

# Register your models here.

# classe para adminnistrar models de Evento. 
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') # Propriedade para mostrar o que irá aparecer no django admin
    list_filter = ('titulo', 'data_evento')

admin.site.register(Evento, EventoAdmin) # associa o evento à classe de administração
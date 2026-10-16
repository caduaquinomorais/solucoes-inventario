from django.contrib import admin
from .models import ItemInventario

@admin.register(ItemInventario)
class ItemInventarioAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na tabela do admin
    list_display = ('codigo', 'equipamento', 'status_equipamento', 'local_fisico', 'responsavel')
    
    # Campos que a barra de pesquisa vai buscar
    search_fields = ('codigo', 'nome_dispositivo', 'responsavel')
    
    # Filtros laterais
    list_filter = ('status_equipamento', 'equipamento', 'local_fisico')
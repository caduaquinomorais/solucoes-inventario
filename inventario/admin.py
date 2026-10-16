from django.contrib import admin
from .models import ItemInventario

@admin.register(ItemInventario)
class ItemInventarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'equipamento', 'status_equipamento', 'local_fisico', 'responsavel')
    search_fields = ('codigo', 'nome_dispositivo', 'responsavel')
    list_filter = ('status_equipamento', 'equipamento', 'local_fisico')
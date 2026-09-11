from django.contrib import admin
from movimentacao import models

@admin.register(models.Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display=('equipamento','codigo','origem','destino','uso','observacao','usuario','data_criacao','status')
    ordering=('-data_criacao',)
    list_per_page=10
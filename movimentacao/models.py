from django.db import models
from django.conf import settings # Referência ao modelo de usuário do projeto

class Movimentacao(models.Model):
    equipamento = models.CharField(
        max_length=30,
        choices=[
            ('notebook_i7','Notebook(Avançado - i7)'),
            ('notebook_i5','Notebook(Básico - i5)'),
            ('workstation','Desktop(Avançado - i7)'),
            ('optiplex','Desktop(Básico - i5)'),
            ('monitor','Monitor'),
            ('mac_mini','Mac mini'),
            ('access_point', 'AP'),
            ('tela_interativa','Tela interativa'),
            ('equipamento_sampacast','Equipamento áudio/vídeo')
        ]
    )
    codigo = models.CharField(max_length=35)
    origem = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    uso = models.CharField(max_length=100,blank=True)
    foto = models.ImageField(blank=True)
    observacao = models.CharField(max_length=250, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente','Pendente'),
            ('processado','Processado'),
            ('descartado','Descartado'),
        ],
        default='pendente'
    )


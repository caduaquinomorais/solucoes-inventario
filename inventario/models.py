from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class ItemInventario(models.Model):
    TIPOS_EQUIPAMENTO = [
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

    equipamento = models.CharField(max_length=30, choices=TIPOS_EQUIPAMENTO)
    nome_dispositivo = models.CharField(max_length=50, blank=True)
    lote = models.CharField(max_length=30, blank=True)
    codigo = models.CharField(max_length=35, unique=True)
    local_fisico = models.CharField(max_length=50)
    setor_equipe = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100, blank=True)
    status_equipamento = models.CharField(
        max_length=20,
        choices=[
            ('disponivel','Disponível'),
            ('em_uso','Em uso'),
            ('manutenção','Em manutenção'),
            ('descartado','Baixa/Descarte'),
        ],
        default='disponivel'
    )
    observacao = models.CharField(max_length=250, blank=True)
    cadastrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()

        if self.status_equipamento == 'em_uso' and not self.responsavel.strip():
            raise ValidationError({
                'responsavel' : 'É obrigatório informar o responsável quando em uso'
            })


    def __str__(self):
        return f'{self.get_equipamento_display()} - {self.codigo}'

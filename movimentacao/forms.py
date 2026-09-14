from django import forms

from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):

    class Meta:
        model = Movimentacao
        fields = [
            'equipamento',
            'codigo',
            'origem',
            'destino',
            'uso',
            'foto',
            'observacao',
        ]
from django.shortcuts import get_object_or_404,render
from .models import Movimentacao


def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data_criacao')

    return render(
        request,
        'movimentacao/lista.html',
        {'movimentacoes': movimentacoes}
    )

def detalhe_movimentacao(request, id):
    movimentacao = get_object_or_404(Movimentacao,id=id)

    return render(
        request,
        'movimentacao/detalhe.html',
        {'movimentacao':movimentacao}
    )
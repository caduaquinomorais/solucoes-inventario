from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect,render
from .models import Movimentacao
from .forms import MovimentacaoForm

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data_criacao')

    return render(
        request,
        'movimentacao/lista.html',
        {'movimentacoes': movimentacoes}
    )

@login_required
def detalhe_movimentacao(request, id):
    movimentacao = get_object_or_404(Movimentacao,id=id)

    return render(
        request,
        'movimentacao/detalhe.html',
        {'movimentacao':movimentacao}
    )

@login_required
def criar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST, request.FILES)

        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.usuario = request.user
            movimentacao.save()

            return redirect(
                'detalhe_movimentacao',
                id=movimentacao.id
            )

    else:
        form = MovimentacaoForm()

    return render(
        request,
        'movimentacao/formulario.html',
        {'form': form}
    )
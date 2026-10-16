from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ItemInventario

@login_required
def lista_inventario(request):
    itens = ItemInventario.objects.all().order_by('equipamento')

    return render(
        request,
        'inventario/lista.html',
        {'itens': itens}
    )
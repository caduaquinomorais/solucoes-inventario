from django.urls import path
from movimentacao import views

urlpatterns = [
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('<int:id>', views.detalhe_movimentacao, name='detalhe_movimentacao'),
]
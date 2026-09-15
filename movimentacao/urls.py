from django.urls import path
from movimentacao import views

urlpatterns = [
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('nova/', views.criar_movimentacao, name= 'criar_movimentacao'),
    path('<int:id>', views.detalhe_movimentacao, name='detalhe_movimentacao'),
    path('<int:id>/editar/', views.editar_movimentacao, name='editar_movimentacao'),
    path('<int:id>/exluir/', views.excluir_movimentacao, name='excluir_movimentacao'),
    path('<int:id>/status/', views.alterar_status, name='alterar_status'),

]
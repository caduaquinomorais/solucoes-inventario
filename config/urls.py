from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movimentacoes/', include('movimentacao.urls')),
    path('conta/', include('django.contrib.auth.urls')),
]

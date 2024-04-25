from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('clientes.urls')),
    path('api/v1/', include('fornecedores.urls')),
    path('api/v1/', include('produtos.urls')),
    path('api/v1/', include('vendas.urls')),
    path('api/v1/', include('compras.urls'))
]

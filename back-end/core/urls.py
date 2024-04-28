from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView


urlpatterns = [
    path('api/v1/', include('clientes.urls')),
    path('api/v1/', include('fornecedores.urls')),
    path('api/v1/', include('produtos.urls')),
    path('api/v1/', include('vendas.urls')),
    path('api/v1/', include('compras.urls')),
    path('api/v1/', include('contas.urls')),
    path('api/v1/login/', UserLoginView.as_view(), name='user-login'),
]

from django.urls import path
from .views import ClienteListCreateAPIView, ClienteRetrieveAPIView, ClienteDestroyAPIView, ClienteUpdateAPIView, ClienteCreateAPIView, ClienteSearchAPIView
from relatorios.views import RelatorioClienteView


urlpatterns = [
    path('clientes/', ClienteListCreateAPIView.as_view(), name='clientes-list'),
    path('cliente/create/', ClienteCreateAPIView.as_view(), name='cliente-create'),
    path('cliente/detail/<int:pk>', ClienteRetrieveAPIView.as_view(), name='cliente-detail'),
    path('cliente/delete/<int:pk>', ClienteDestroyAPIView.as_view(), name='cliente-delete'),
    path('cliente/update/<int:pk>', ClienteUpdateAPIView.as_view(), name='cliente-update'),
    path('cliente/search/', ClienteSearchAPIView.as_view(), name='cliente-search'),
    path('cliente/relatorio/', RelatorioClienteView.as_view(), name='cliente-relatorio')
]
from django.urls import path
from .views import VendaListAPIView, VendaCreateAPIView, VendaRetrieveAPIView, VendaDestroyAPIView, VendaUpdateAPIView, VendaSearch, VendaEstornoView
from relatorios.views import RelatorioVendaView

urlpatterns = [
    path('vendas/', VendaListAPIView.as_view(), name='vendas-list'),
    path('venda/create/', VendaCreateAPIView.as_view(), name='venda-create'),
    path('venda/detail/<int:pk>', VendaRetrieveAPIView.as_view(), name='venda-detail'),
    path('venda/delete/<int:pk>', VendaDestroyAPIView.as_view(), name='venda-delete'),
    path('venda/update/<int:pk>', VendaUpdateAPIView.as_view(), name='venda-update'),
    path('venda/search/', VendaSearch.as_view(), name='venda-search'),
    path('venda/relatorio/', RelatorioVendaView.as_view(), name='venda-relatorio'),
    path('venda/estorno/', VendaEstornoView.as_view(), name='venda-estorno')
]
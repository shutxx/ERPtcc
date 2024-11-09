from django.urls import path
from .views import ProdutoListAPIView, ProdutoCreateAPIView, ProdutoRetrieveAPIView, ProdutoDestroyAPIView, ProdutoUpdateAPIView, ProdutoSearch
from relatorios.views import RelatorioProdutoView

urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='produtos-list'),
    path('produto/create/', ProdutoCreateAPIView.as_view(), name='produto-create'),
    path('produto/detail/<int:pk>', ProdutoRetrieveAPIView.as_view(), name='produto-detail'),
    path('produto/delete/<int:pk>', ProdutoDestroyAPIView.as_view(), name='produto-delete'),
    path('produto/update/<int:pk>', ProdutoUpdateAPIView.as_view(), name='produto-update'),
    path('produto/search/', ProdutoSearch.as_view(), name='produto-search'),
    path('produto/relatorio/', RelatorioProdutoView.as_view(), name='produto-relatorio')
]
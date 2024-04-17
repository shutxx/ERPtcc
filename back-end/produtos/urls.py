from django.urls import path
from .views import ProdutoListAPIView, ProdutoCreateAPIView, ProdutoRetrieveAPIView, ProdutoDestroyAPIView, ProdutoUpdateAPIView

urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='produto-list'),
    path('produto/create/', ProdutoCreateAPIView.as_view(), name='produto-create'),
    path('produto/detail/<int:pk>', ProdutoRetrieveAPIView.as_view(), name='fornecedor-detail'),
    path('produto/delete/<int:pk>', ProdutoDestroyAPIView.as_view(), name='fornecedor-delete'),
    path('produto/update/<int:pk>', ProdutoUpdateAPIView.as_view(), name='fornecedor-update')
]
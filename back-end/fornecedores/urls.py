from django.urls import path
from .views import FornecedorListAPIView, FornecedorCreateAPIView, FornecedorRetrieveAPIView, FornecedorDestroyAPIView, FornecedorUpdateAPIView

urlpatterns = [
    path('fornecedores/', FornecedorListAPIView.as_view(), name='fornecedores-list'),
    path('fornecedor/create/', FornecedorCreateAPIView.as_view(), name='fornecedor-create'),
    path('fornecedor/detail/<int:pk>', FornecedorRetrieveAPIView.as_view(), name='fornecedor-detail'),
    path('fornecedor/delete/<int:pk>', FornecedorDestroyAPIView.as_view(), name='fornecedor-delete'),
    path('fornecedor/update/<int:pk>', FornecedorUpdateAPIView.as_view(), name='fornecedor-update')
]
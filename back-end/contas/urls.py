from django.urls import path
from .views import ContasPagar, ContasReceber

urlpatterns = [
    path('contas-pagar/', ContasPagar.ContaPagarListAPIView.as_view(), name='conta-pagar-list'),
    path('conta-pagar/create/', ContasPagar.ContaPagarCreateAPIView.as_view(), name='conta-pagar-create'),
    path('conta-pagar/detail/<int:pk>', ContasPagar.ContaPagarRetrieveAPIView.as_view(), name='conta-pagar-detail'),
    path('conta-pagar/update/<int:pk>', ContasPagar.ContaPagarUpdateAPIView.as_view(), name='conta-pagar-update'),
    path('conta-pagar/delete/<int:pk>', ContasPagar.ContaPagarDestroyAPIView.as_view(), name='conta-pagar-delete'),

    path('contas-receber/', ContasReceber.ContaReceberListAPIView.as_view(), name='conta-receber-list'),
    path('conta-receber/create/', ContasReceber.ContaReceberCreateAPIView.as_view(), name='conta-receber-create'),
    path('conta-receber/detail/<int:pk>', ContasReceber.ContaReceberRetrieveAPIView.as_view(), name='conta-receber-detail'),
    path('conta-receber/update/<int:pk>', ContasReceber.ContaReceberUpdateAPIView.as_view(), name='conta-receber-update'),
    path('conta-receber/delete/<int:pk>', ContasReceber.ContaReceberDestroyAPIView.as_view(), name='conta-receber-delete'),
]

from django.urls import path
from .views import CompraListCreateAPIView

urlpatterns = [
    path('compras/', CompraListCreateAPIView.as_view(), name='compras-list'),
    #path('compra/create/', VendaCreateAPIView.as_view(), name='compra-create'),
    #path('compra/detail/<int:pk>', VendaRetrieveAPIView.as_view(), name='compra-detail'),
    #path('compra/delete/<int:pk>', VendaDestroyAPIView.as_view(), name='compra-delete'),
    #path('compra/update/<int:pk>', VendaUpdateAPIView.as_view(), name='compra-update')
]
from django.urls import path
from .views import CompraListAPIView, CompraCreateAPIView, CompraRetrieveAPIView, CompraUpdateAPIView, CompraDestroyAPIView

urlpatterns = [
    path('compras/', CompraListAPIView.as_view(), name='compras-list'),
    path('compra/create/', CompraCreateAPIView.as_view(), name='compra-create'),
    path('compra/detail/<int:pk>', CompraRetrieveAPIView.as_view(), name='compra-detail'),
    path('compra/delete/<int:pk>', CompraDestroyAPIView.as_view(), name='compra-delete'),
    path('compra/update/<int:pk>', CompraUpdateAPIView.as_view(), name='compra-update')
]
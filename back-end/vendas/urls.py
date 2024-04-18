from django.urls import path
from .views import VendaListCreateAPIView

urlpatterns = [
    path('vendas/', VendaListCreateAPIView.as_view(), name='vendas-list')
]
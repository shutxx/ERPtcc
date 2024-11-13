from rest_framework import generics
from rest_framework.views import APIView
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ClienteListCreateAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

class ClienteCreateAPIView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ClienteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ClienteDestroyAPIView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ClienteUpdateAPIView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ClienteSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            clienteSeach = Cliente.objects.filter(
                Q(NomePessoa__icontains=query) | Q(CPFouCNPJ__icontains=query)
            )
        else:
            clienteSeach = Cliente.objects.all()
        pagination_class = PageNumberPagination()
        pagination_class.page_size = 10
        result_page = pagination_class.paginate_queryset(clienteSeach, request)
        serializer_class = ClienteSerializer(result_page, many=True)
        return pagination_class.get_paginated_response(serializer_class.data)
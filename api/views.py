from django.shortcuts import render
from .models import Mascotas
from .serializers import MascotasSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

class MascotasPagination(PageNumberPagination):
    page_size = 6  # Paginación predeterminada

class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all().order_by('-fecha_registro')
    serializer_class = MascotasSerializer
    pagination_class = MascotasPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['edad', 'fecha_registro']
    search_fields = ['nombre', 'especie', 'raza', 'sexo']


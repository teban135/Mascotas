from django.shortcuts import render
from .models import Mascotas
from .serializers import MascotasSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .filters import MascotasFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

class MascotasPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 9

class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all().order_by('-fecha_registro')
    serializer_class = MascotasSerializer
    pagination_class = MascotasPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = MascotasFilter
    ordering_fields = ['edad', 'fecha_registro']
    search_fields = ['nombre', 'especie', 'raza', 'sexo']

    @action(detail=False, methods=['get'])
    def opciones_filtros(self, request):
        # Obtener especies y razas únicas
        especies = Mascotas.objects.values('especie').distinct()
        razas = Mascotas.objects.values('raza').distinct()

        # Formatear la respuesta
        data = {
            'especies': [item['especie'] for item in especies],
            'razas': [item['raza'] for item in razas]
        }
        return Response(data)
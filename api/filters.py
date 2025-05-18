import django_filters
from .models import Mascotas

class MascotasFilter(django_filters.FilterSet):
    min_edad = django_filters.NumberFilter(field_name="edad", lookup_expr='gte')
    max_edad = django_filters.NumberFilter(field_name="edad", lookup_expr='lte')
    especie = django_filters.CharFilter(field_name="especie", lookup_expr='exact', method='clean_filter')
    raza = django_filters.CharFilter(field_name="raza", lookup_expr='exact', method='clean_filter')
    sexo = django_filters.CharFilter(field_name="sexo", lookup_expr='exact')

    def clean_filter(self, queryset, name, value):
        if value:
            value = value.strip() # Eliminar espacios al inicio/fin
        return queryset.filter(**{name: value})

    class Meta:
        model = Mascotas
        fields = ['especie', 'raza', 'sexo', 'min_edad', 'max_edad']

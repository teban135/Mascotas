from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MascotasViewSet 

#creamos el enrutados y registramos el viwset
router = DefaultRouter()
router.register(r'mascotas',MascotasViewSet)

#incluir las urls del enrutador 
urlpatterns =[
    path('',include(router.urls)),
]
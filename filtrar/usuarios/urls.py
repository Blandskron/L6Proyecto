from django.urls import path
from .views import lista_ventas

urlpatterns = [
    path('ventas/', lista_ventas, name='lista_ventas'),
]

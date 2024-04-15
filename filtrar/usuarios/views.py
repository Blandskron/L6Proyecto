from django.shortcuts import render
from .models import Venta

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})


def lista_ventas(request):
    ventas = Venta.objects.all()

    # Obtener los parámetros de filtro del request
    fecha_inicio_filtro = request.GET.get('fecha_inicio')
    fecha_fin_filtro = request.GET.get('fecha_fin')
    vendedor_filtro = request.GET.get('vendedor')

    # Aplicar el filtro si se proporcionan los parámetros
    if fecha_inicio_filtro and fecha_fin_filtro:
        ventas = ventas.filter(fecha__range=[fecha_inicio_filtro, fecha_fin_filtro])
    if vendedor_filtro:
        ventas = ventas.filter(vendedor__username=vendedor_filtro)

    return render(request, 'lista_ventas.html', {'ventas': ventas, 'fecha_inicio': fecha_inicio_filtro, 'fecha_fin': fecha_fin_filtro, 'vendedor_filtro': vendedor_filtro})
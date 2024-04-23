# L6Proyecto

# Crearemos el entorno Virtual
```
    python -m venv venv
    venv\Scripts\activate
```

# Intalar Django
```
    pip install django
```

# Crear proyecto
```
    django-admin startproject filtrar
```

# Crear aplicacion
```
    cd filtrar
    python manage.py startapp usuarios
```

# Agregamos la aplicacion a nuestro setting.py
```
    INSTALLED_APPS = [
        'usuarios',
    ]
```


# Modificamos nuestros archivos "views.py" - "models.py" - "admin.py"
```
    #views.py
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
```
```
    #models.py
    from django.db import models
    from django.contrib.auth.models import User

    class Venta(models.Model):
        vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
        fecha = models.DateField()
        cantidad = models.IntegerField()
        cliente = models.CharField(max_length=100)
        producto = models.CharField(max_length=100)
```
```
    #admin.py
    from django.contrib import admin
    from django.contrib.auth.models import Group
    from .models import Venta

    admin.site.register(Venta)
    admin.site.unregister(Group)
```

# Creamos los archivos "urls.py" - "signals.py"
```
    #ursl.py
    from django.urls import path
    from .views import lista_ventas

    urlpatterns = [
        path('ventas/', lista_ventas, name='lista_ventas'),
    ]
```
```
    #signals.py
    from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Crear grupos si no existen
    for group_name in ['GERENTE', 'SUPERVISOR', 'VENDEDOR']:
        group, created = Group.objects.get_or_create(name=group_name)

    # Definir permisos para cada grupo
    permissions = {
        'GERENTE': ['view_venta', 'change_venta'],
        'SUPERVISOR': ['view_venta'],
        'VENDEDOR': ['view_venta'],
    }

    for group_name, codenames in permissions.items():
        group = Group.objects.get(name=group_name)
        group.permissions.set(Permission.objects.filter(codename__in=codenames))
```

# creamos una carpeta llamada "TEMPLATES" y dentro un archivo html llamado "lista_ventas.html"
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Ventas</title>
</head>
<body>
    <h1>Lista de Ventas</h1>

    <!-- Formulario de filtro -->
    <form action="" method="GET">
        <label for="fecha_inicio">Fecha inicial:</label>
        <input type="date" id="fecha_inicio" name="fecha_inicio" value="{{ fecha_inicio }}">
        <br>
        <label for="fecha_fin">Fecha final:</label>
        <input type="date" id="fecha_fin" name="fecha_fin" value="{{ fecha_fin }}">
        <br>
        <label for="filtro_vendedor">Filtrar por nombre del vendedor:</label>
        <input type="text" id="filtro_vendedor" name="vendedor" value="{{ vendedor_filtro }}">
        <button type="submit">Filtrar</button>
    </form>

    <ul>
        {% for venta in ventas %}
            <li>{{ venta.fecha }} - {{ venta.cantidad }} (Vendedor: {{ venta.vendedor.username }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```
    
# Realizamos las migraciones
```
    python manage.py makemigrations
    python manage.py migrate
```

# Creamos el super usuario
```
    python manage.py createsuperuser
```

# Corremos la aplicacion
```
    python manage.py runserver
```

# Entramos al admin para agregar data en nuestra tabla venta
# Luego entramos a ventas para filtrar la informacion de la tabla

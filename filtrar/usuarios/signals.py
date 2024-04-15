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

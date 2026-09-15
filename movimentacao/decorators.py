from django.core.exceptions import PermissionDenied


def administrador_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(
            name='Administradores'
        ).exists():
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper
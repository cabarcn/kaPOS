from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSoporte(BasePermission):
    """
    Permite acceso solo a usuarios autenticados con rol SOPORTE.
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "rol", None) == "SOPORTE"
        )


class IsSoporteOrReadOnly(BasePermission):
    """
    Permite lectura a cualquiera autenticado, pero solo SOPORTE puede modificar.
    """
    def has_permission(self, request, view):
        user = request.user

        # Lecturas (GET, HEAD, OPTIONS) → solo requieren estar autenticado
        if request.method in SAFE_METHODS:
            return bool(user and user.is_authenticated)

        # Escrituras → solo SOPORTE
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "rol", None) == "SOPORTE"
        )

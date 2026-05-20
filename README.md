# kaPOS

Sistema orientado a la gestión de donaciones, diseñado para ordenar procesos de registro, consulta y control sobre aportes, usuarios y operaciones asociadas.

## Problema que aborda

La gestión de donaciones suele involucrar múltiples actores, estados de pago, medios de recaudación y trazabilidad operativa. Cuando esa información se maneja con herramientas dispersas o procesos manuales, cuesta mantener consistencia, auditar movimientos y escalar el sistema.

## Solución propuesta

kaPOS plantea una base backend para centralizar la lógica de negocio relacionada con donaciones y exponerla mediante una API robusta. El proyecto busca ser una plataforma sobre la cual se pueda construir una operación más clara, segura y mantenible.

## Qué resuelve

- centraliza la información operativa de donaciones
- organiza autenticación y acceso a través de una API
- prepara una base sólida para integraciones con frontend, dashboards o procesos administrativos

## Arquitectura y stack

Actualmente el repositorio está enfocado en backend, con una arquitectura típica de API web moderna sobre Django.

### Backend

- Django 5.2
- Django REST Framework
- PostgreSQL
- autenticación JWT con `djangorestframework-simplejwt`

### Soporte y tooling

- `drf-spectacular` para documentación OpenAPI / Swagger
- `django-cors-headers` para integración con frontend
- `pytest` y `pytest-django` para testing
- `gunicorn` y `whitenoise` para despliegue

## Enfoque del sistema

El proyecto está bien posicionado para servir como backend de una plataforma de recaudación o gestión institucional, donde el frontend puede evolucionar por separado sin comprometer la lógica central.

## Diferenciales

- Se presenta como una base backend realista, no solo como CRUD aislado.
- La elección de JWT, documentación de API y testing lo acerca a un estándar más profesional.
- Tiene continuidad natural con proyectos analíticos como `DW_KApos`, lo que refuerza una narrativa completa: operación + datos + reporting.

## Estado del proyecto

Backend en desarrollo con orientación clara a producto. El valor actual está en la base técnica y en la definición de una arquitectura preparada para crecer.

## Cómo ejecutarlo

```bash
git clone https://github.com/cabarcn/kaPOS.git
cd kaPOS
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

Luego configura tu base de datos PostgreSQL, variables de entorno si corresponden, y ejecuta:

```bash
python manage.py migrate
python manage.py runserver
```

## Próximos pasos posibles

- completar frontend de operación
- incorporar flujos de recaudación más específicos
- agregar reporting y auditoría transaccional
- fortalecer permisos, roles y trazabilidad de cambios

## Autor

Cristopher Abarca

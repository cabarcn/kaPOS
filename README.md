# kaPOS

Sistema orientado a la gestion de donaciones, disenado para ordenar procesos de registro, consulta y control sobre aportes, usuarios y operaciones asociadas.

## Problema que aborda

La gestion de donaciones suele involucrar multiples actores, estados de pago, medios de recaudacion y trazabilidad operativa. Cuando esa informacion se maneja con herramientas dispersas o procesos manuales, cuesta mantener consistencia, auditar movimientos y escalar el sistema.

## Solucion propuesta

kaPOS plantea una base backend para centralizar la logica de negocio relacionada con donaciones y exponerla mediante una API robusta. El proyecto busca ser una plataforma sobre la cual se pueda construir una operacion mas clara, segura y mantenible.

## Que resuelve

- centraliza la informacion operativa de donaciones
- organiza autenticacion y acceso a traves de una API
- prepara una base solida para integraciones con frontend, dashboards o procesos administrativos

## Arquitectura y stack

Actualmente el repositorio esta enfocado en backend, con una arquitectura tipica de API web moderna sobre Django.

### Backend

- Django 5.2
- Django REST Framework
- PostgreSQL
- autenticacion JWT con `djangorestframework-simplejwt`

### Soporte y tooling

- `drf-spectacular` para documentacion OpenAPI / Swagger
- `django-cors-headers` para integracion con frontend
- `pytest` y `pytest-django` para testing
- `gunicorn` y `whitenoise` para despliegue

## Enfoque del sistema

El proyecto esta bien posicionado para servir como backend de una plataforma de recaudacion o gestion institucional, donde el frontend puede evolucionar por separado sin comprometer la logica central.

## Diferenciales

- Se presenta como una base backend realista, no solo como CRUD aislado.
- La eleccion de JWT, documentacion de API y testing lo acerca a un estandar mas profesional.
- Tiene continuidad natural con proyectos analiticos como `DW_KApos`, lo que refuerza una narrativa completa: operacion + datos + reporting.

## Estado del proyecto

Backend en desarrollo con orientacion clara a producto. El valor actual esta en la base tecnica y en la definicion de una arquitectura preparada para crecer.

## Como ejecutarlo

```bash
git clone https://github.com/cabarcn/kaPOS.git
cd kaPOS
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
copy .env.example .env
```

En Linux o macOS:

```bash
source .venv/bin/activate
cp .env.example .env
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

Luego configura tu base de datos PostgreSQL, ajusta las variables del archivo `.env` y ejecuta:

```bash
python manage.py migrate
python manage.py runserver
```

## Proximos pasos posibles

- completar frontend de operacion
- incorporar flujos de recaudacion mas especificos
- agregar reporting y auditoria transaccional
- fortalecer permisos, roles y trazabilidad de cambios

## Autor

Cristopher Abarca

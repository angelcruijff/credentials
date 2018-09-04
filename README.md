# Credentials
Proyecto para guardar passwords. El usuario define los metadatos de cada credencial que desee crear.

## Contenido

* [Run With Docker](#run-with-docker)

## Run With Docker
Si se va a ejecutar la aplicación por primera vez, se necesitan correr los siguientes comandos

- Ejecutar la migración de la base de datos para la creación de las tablas y la base de datos.
```
docker-compose run web python manage.py migrate
```

- Crear super usuario para acceder a la parte administrativa
```
docker-compose run web python manage.py createsuperuser
```

- Ejecutar la aplicación
```
docker-compose up -d web

```

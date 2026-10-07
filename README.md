# Practica 4 para TSCC

## Instrucciones

Instalacion de Dependencias

```bash
# pip
python -m venv .venv
source .venv/bin/activate
pip install .
```

```bash
# uv
uv sync
```

Levantar PostgreSQL

```bash
docker composer up -d
docker ps
```

Conectarse a la Base de Datos

```bash
cd proyecto_django/back_end_django && ./pgres.bash
```

Listar las tablas dentro de la Base de Datos

```sql
\dt
```

Preparar el entorno con la Base de Datos

```bash
python3 manage.py makemigrations gestion_usuarios
python3 manage.py makemigrations gestion_productos
python3 manage.py migrate
python3 manage.py check
python3 manage.py runserver
```

```bash
# uv
uv run manage.py makemigrations gestion_usuarios
uv run manage.py makemigrations gestion_productos
uv run manage.py migrate
uv run manage.py check
uv run manage.py runserver
```

Visualizacion de la API

```
http://127.0.0.1:8000/swagger/
```

# Polaris - Sistema de Gestión de Empleados

## Descripción

Polaris es una aplicación web desarrollada con **Django** que permite administrar la información de empleados y cargos dentro de una organización. El proyecto implementa operaciones CRUD (Crear, Leer, Actualizar y Eliminar) utilizando dos enfoques de Django:

- Function Based Views (FBV)
- Class Based Views (CBV)

El objetivo del proyecto es demostrar el funcionamiento de ambos tipos de vistas y su implementación en un sistema de gestión.

---

## Características

- Página principal con estadísticas.
- Gestión de cargos.
- Gestión de empleados.
- CRUD completo para cargos.
- CRUD completo para empleados.
- Implementación mediante Function Based Views.
- Implementación mediante Class Based Views.
- Base de datos SQLite.

---

## Tecnologías utilizadas

- Python 3
- Django 6
- HTML5
- CSS3
- SQLite

---

## Estructura del proyecto

```
Proyecto G_G/
│
├── manage.py
├── db.sqlite3
├── polaris/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── views_fbv.py
│   ├── views_cbv.py
│   ├── urls_fbv.py
│   ├── urls_cbv.py
│   ├── templates/
│   └── migrations/
│
└── polaris_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## Modelos

### Cargo

Representa el cargo que ocupa un empleado.

Campos:

- Nombre
- Descripción

### Empleado

Representa la información de un empleado.

Campos:

- Nombres
- Apellidos
- Correo electrónico
- Sueldo
- Fecha de ingreso
- Cargo (relación con la tabla Cargo)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/repositorio.git
```

### 2. Entrar al proyecto

```bash
cd Proyecto_G_G
```

### 3. Crear un entorno virtual

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install django
```

o

```bash
pip install -r requirements.txt
```

---

## Ejecutar las migraciones

```bash
python manage.py migrate
```

---

## Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir el navegador en:

```
http://127.0.0.1:8000/
```

---

## Funcionalidades

### Inicio

La página principal muestra un resumen con:

- Total de cargos registrados.
- Total de empleados registrados.

### Gestión de cargos

Permite:

- Registrar cargos.
- Visualizar cargos.
- Editar cargos.
- Eliminar cargos.

### Gestión de empleados

Permite:

- Registrar empleados.
- Consultar empleados.
- Modificar empleados.
- Eliminar empleados.

---

## Patrón utilizado

El proyecto implementa el patrón **Modelo - Vista - Plantilla (MVT)** propio de Django.

Se incluyen dos implementaciones de las vistas:

### Function Based Views (FBV)

Las operaciones CRUD son implementadas mediante funciones.

### Class Based Views (CBV)

Las operaciones CRUD son implementadas utilizando clases genéricas de Django.

---

## Base de datos

Se utiliza **SQLite**, la base de datos predeterminada de Django.

No requiere configuración adicional para pruebas o desarrollo.

---

## Autor

Proyecto desarrollado como práctica académica utilizando el framework Django para la implementación de operaciones CRUD y comparación entre Function Based Views y Class Based Views.

---

## Licencia

Este proyecto tiene fines educativos y académicos.
# **log-hours app v1.0.0**
Aplicación que administra el Registro de horas
de un proyecto como apoyo a la gestión del mismo. Este es
el repositorio [log-hours](https://github.com/DeveloperSenior/log-hours.git).

#Dependencias

1. [Git v2.36.+](https://git-scm.com/downloads).
2. [Python v3.9](https://www.python.org/downloads/).
3. Django v4.0.4 (**Se instala por dependencia `pip` más adelante**) framework para el uso Model Vista Template.
4. Psycopg2 v2.9.3 (**Se instala por dependencia `pip` más adelante**) Driver PostgreSQL para Python.
5. [MDBootstrap](https://mdbootstrap.com/docs/) (Se utiliza la dependencia [CDN](https://mdbootstrap.com/docs/b4/jquery/getting-started/cdn/) de Material Design).
6. [Font Awesome](https://fontawesome.com) (Se utiliza dependencia [CDN](https://use.fontawesome.com/releases/v6.1.1/css/all.css)).
7. Para temas de desarrollo se recomienda [VS Code](https://code.visualstudio.com/download)
   o [PyCharm](https://www.jetbrains.com/pycharm/download/) o el editor que mejor se acomode.
   
   **NOTA**: Estos editores tiene integrado la terminal para ejecutar comandos `script` que más adelante
   vamos a utilizar.
8. Terminal UNIX o DOS para ejecutar `script` puede ser la que tiene el sistema operativo o un emulador
   de consola [Cmder](https://cmder.net).

#Instalación

* Se debe clonar el repositorio. 
  abrir la terminal `shell` o `cmd` ingrese el siguiente
  comando `script`.
```
Linux - Unix - MacOS - Windows

git clone https://github.com/DeveloperSenior/log-hours.git
```
* Se ingresa a la carpeta clonada `log-hours` luego a la raíz del proyecto `LogHours`.
```
Linux - Unix - MacOS - Windows
cd log-hours
cd LogHours
```
* Se virtualiza el proyecto para el intérprete `Python` en `venv`.
```
Linux - Unix - MacOS - Windows

python -m venv env
source env/bin/activate
```
o
```
Linux - Unix - MacOS - Windows

python3.9 -m venv env
source env/bin/activate
```

```
Windows

python -m venv env
env/Scripts/activate
```
o
```
Windows

python3.9 -m venv env
env/Scripts/activate
```
**NOTA**: Tener en cuenta que en PyCharm se debe configurar el interpreter de Python (Pero eso se sale del alcance de este documento).
* Se ejecuta `script` para instalar dependencias del proyecto.
```
# Linux - Unix - MacOS - Windows

pip install -r requirements.txt
```
* Revisar el archivo de configuración `LogHours/settings.py` para configurar la Base de datos PostgrSQL.
 
 **NOTA:** Se tiene una configuración por defecto.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<NOMBRE_BD>',
        'USER': '<USUARIO_BD>',
        'PASSWORD': '<PASSWORD_BD>',
        'HOST': '<HOST_BD>',
        'PORT': '<PORT_BD>',
    }
}
```
* Migrar el modelo de datos de `Django`y `LogHours`
```
# Linux - Unix - MacOS - Windows

python manage.py migrate
```
```
# Linux - Unix - MacOS - Windows

python3.9 manage.py migrate
```
* Crear Super Usuario que administrara todo el sistema.
  
  **NOTA:** Tener cuidado que es un usuario ROOT del sistema y tiene acceso
   a todo, `Esta información es almacenada en la base de datos`
```
# Linux - Unix - MacOS - Windows

python manage.py createsuperuser
```
o
```
# Linux - Unix - MacOS - Windows

python3.9 manage.py createsuperuser
```
Ingresar toda la información solicitada (Guardar usuario y clave para poder ingresar al sistema de manera que lo pueda usar más adelante).
```
# Output

Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.
```

* Finalmente se levanta el servidor Django existen 2 opciones.

1. Borrando el modelo de datos y migrándolo totalmente desde cero 
   
     (**NOTA:** Este comando borra las tablas por completo tenga en cuenta que si no es la 
     primera vez que se ejecuta será borrada toda la información y tocara ejecutar el paso
     de la `creación del superusuario`)
```
# Linux - Unix - MacOS

./run-app-migrate.sh

# Windows

run-app-migrate.bat
```
2. Ejecutando la aplicación normal
```
# Linux - Unix - MacOS

./run-app.sh

# Windows

run-app.bat
```

```
# Output

System check identified no issues (0 silenced).
Django version 4.0.4, using settings 'LogHours.settings'
Starting development server at http://127.0.0.1:8000/
```
* Abrir la aplicación en el navegador `http://127.0.0.1:8000/` para este ejemplo 
  el host es `127.0.0.1` reemplaza por la `ip o host` del entorno de ejecución.
* Para administrar los maestros, usuarios y grupos ingresar a `http://127.0.0.1:8000/admin/` con las credenciales
 del `superusuario` anteriormente creado.

#Instalación en un contenedor DOCKER
Tenga en cuenta el archivo `Dockerfile` para crear la imagen de la app
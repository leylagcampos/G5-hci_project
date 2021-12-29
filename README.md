# Web Gestion de Hospital
### Tecnologías
- Frontend
	- HTML5,CSS3,JQuery,Bootstrap
- Backend
    - Django framework
- Database
    - SQLite
### Local Setup
<!--
1. Clonar el repositorio
2. Abrir el terminal bash en el Visual Code (recomendado) , o hacer "Git bash here" dentro de la carpeta clonada
3. Verificar la version de python con `python --version`.
	- Si tiene varias versiones le aparecerá la ultima que instaló.No es un problema,pero tambien debe tener la version 3.8.2 para activar el entorno virtual de este proyecto.
	- Para tener la version de python 3.8.2., seleccionar "Windows x86-64 executable installer " de https://www.python.org/downloads/release/python-382/ para descargar e instalelo.
4. Configurar el entorno virtual:	
	- Ejecute el comando `pipenv shell` para activar el entorno virtual.Ejecutelo denuevo las veces que quiera verificar que está activo.
	- Puede verificar la version de python del entorno virtual con `python --version`,y deberá mostrar la version 3.8.2.
	- Ejecute el comando `pipenv install` para la instalacion de las dependencias del pipfile.
5. Run `python manage.py runserver`.
6. Go to `127.0.0.1::8000` in your web browser.
-->
1. Este proyecto corre con python 3.8.2., para obtenerlo seleccionar "Windows x86-64 executable installer " de https://www.python.org/downloads/release/python-382/ para descargar e instalelo.
2. Clone y abra el proyecto en Visual Code,luego abra la terminal (bash), haga lo siguiente:
	- Ejecute el comando `pipenv shell` para activar el entorno virtual.Ejecutelo denuevo las veces que quiera verificar que está activo.
	- Puede verificar la version de python del entorno virtual con `python --version`,y deberá mostrar la version 3.8.2.
	- Ejecute el comando `pipenv install` para la instalacion de las dependencias del pipfile.
3. Ejecute el siguiente comando: `python manage.py runserver`.
4. Abra `127.0.0.1::8000` en su navegador.
#### Observaciones y Comandos de pipenv :
	- Verificar la version de python con `python --version`.Si tiene varias versiones le aparecerá la ultima que instaló.No es un problema,pero tambien debe tener la version 3.8.2 para activar el entorno virtual de este proyecto.
	- Si el comando pipenv no funciona,instalelo con el siguiente comando : `pip3 install pipenv`.
	- Si desea salir del entorno virtual ejecute `exit`,para volver a entrar solo use `pipenv shell`
	- Para ver dependencias instaladas use `pipenv lock -r` y para verlas de manera jerárquica `pipenv graph`
	- Para borrar el entorno use `pipenv --rm` y repita los pasos de "Configurar entorno virtual" 

## Credenciales de prueba para la app 
- preguntame

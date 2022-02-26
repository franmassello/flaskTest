# Test Tecnico API REST en Python
API REST hecha con Python la cual se encarga de calcular el gcd (greatest common divisor) y nos lo devuelve.

# Indice
- Lenguajes y librerias usadas
- Como usar la API
- Testing
- Documentacion API Postman
- Estructura de codigo
- Docker

# Lenguajes y librerias usadas
- Python
- Flask
- Flask-Restful
- Pytest
- Docker (tecnologia)

# Como usar la API
SIN DOCKER:
- Es necesario tener Python 3.7 o mayor
- Editor de codigo VSCode o PyCharm 
- Bajar el repo usando git clone https://github.com/franmassello/flaskTest.git
- Hacer pip install requirements.txt
- Correr el archivo main.py
De esta manera tendriamos corriendo la API en nuestro localhost, mientras se siga ejecutando la terminal.
Para ver como usar docker hacer click aqui

# Testing
Los tests en esta API son dos archivos, en uno se testea la funcion gdc_euclides y en el otro archivo se testea el funcionamiento de la API.
Para correr los tests hay que ejecutar en la carpeta /flaskTest el comando "pytest". 

# Documentacion API Postman
https://documenter.getpostman.com/view/19198278/UVkpQGdB

# Estructura de codigo
- /flaskTest
  - /src
    - /functions
      - gcd_euclides.py Archivo donde se define la funcion principal de la API
    - main.py Archivo principal de la API
  - /tests
    - test_functions.py Archivo donde se testea la funcion principal
    - test_routes.py Archivo donde se testea que ande toda la aplicacion de Flask
  - Entrevista backend - Pipet.pdf
  - README.md

# Docker
Pasos:
- Descargar Docker Desktop
- Instalar Docker Desktop
- En /flaskTest ejecutar:
  - "docker build -t flasktest ." para crear la app en docker
  - "docker image ls" para ver que se haya creado la app
  - "docker run -it -p 5000:5000 flasktest" para correr la app 

# Test Tecnico API REST en Python
API REST hecha con Python la cual se encarga de calcular el gcd (greatest common divisor) y nos lo devuelve.

# Indice
- Lenguajes y librerias usadas
- Como usar la API
- Testing
- Documentacion API Postman
- Estructura de codigo

# Lenguajes y librerias usadas
- Python
- Flask
- Flask-Restful
- Pytest

# Como usar la API
- Es necesario tener Python 3.7 o mayor
- Editor de codigo VSCode o PyCharm 
- Bajar el repo usando git clone https://github.com/franmassello/flaskTest.git
- Hacer pip install Flask, marshmallow, flask_restful, pytest
- Correr el archivo main.py

# Testing
- pytest en /flasktest


# Documentacion API Postman
# Estructura de codigo
- /flaskTest
  - /src
    - /functions
      - gcd_euclides.py Archivo donde se define la funcion principal de la API
    - main.py Archivo principal de la API
  - /tests
    - test.py Archivo principal de tests
  - Entrevista backend - Pipet.pdf
  - README.md

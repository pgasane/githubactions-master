# Los que no tengáis poetry
1. pip install poetry
2. conda install -c conda-forge poetry

# Creamos plantilla
Ejecutar poetry init
1. Package name: modeltools
2. Version: ENTER
3. Description: ENTER
4. Author: vuestro nombre / ENTER
5. License: ENTER
6. Versión Python: ENTER
7. Would you like to define your main dependencies interactively?: NO
8. NO
9. Confirm. YES

# Crear paquete / docs / tests
Ejercicio: Crear tres carpetas:
A) modeltools
B) docs
C) tests

- Crear __init__.py
- poetry build

# Declarar dependencia
1. poetry add numpy
2. Comrpobais que en pyproject aparece numpy
3. git add de:
- pyproject.toml
- poetry.lock
- preprocessing.py
4. commit y push

# Distribuir el paquete
- cambio de versión a la 0.1.1
- poetry build
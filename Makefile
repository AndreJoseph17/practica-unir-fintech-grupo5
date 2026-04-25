# Variable para el nombre del script
SCRIPT = main.py
PYTHON = python3

# Objetivo por defecto: ejecutar la aplicación
run:
	$(PYTHON) $(SCRIPT)

# Objetivo para ejecutar con parámetros (ejemplo: orden descendente)
run-desc:
	$(PYTHON) $(SCRIPT) --desc

# Objetivo para limpiar archivos basura de Python (__pycache__)
clean:
	rm -rf __pycache__
	find . -type f -name "*.pyc" -delete

# Objetivo para instalar dependencias (si tuvieras un requirements.txt)
install:
	pip install -r requirements.txt
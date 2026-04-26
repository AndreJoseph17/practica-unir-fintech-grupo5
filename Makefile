# Variable para el nombre del script
SCRIPT = main.py
PYTHON = python3

# Objetivo para instalar dependencias (si tuvieras un requirements.txt)
install:
	pip install -r requirements.txt

# Instalación de dependencias (si existiera un requirements.txt en el futuro)
install:
	pip install -r requirements.txt

# Directiva para ejecutar en local sin Docker
run-local:
	@echo "Ejecutando aplicación en local..."
	$(PYTHON) $(SCRIPT)

# Objetivo para ejecutar con parámetros (ejemplo: orden descendente)
run-desc:
	$(PYTHON) $(SCRIPT) --desc


# Limpieza de archivos temporales de Python
clean:
	rm -rf __pycache__
	rm -rf *.pyc
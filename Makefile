# Variables
PYTHON = python3
SCRIPT = main.py

# Instalación de dependencias (si existiera un requirements.txt en el futuro)
install:
	pip install -r requirements.txt

# Directiva para ejecutar en local sin Docker
run-local:
	@echo "Ejecutando aplicación en local..."
	$(PYTHON) $(SCRIPT)

# Limpieza de archivos temporales de Python
clean:
	rm -rf __pycache__
	rm -rf *.pyc
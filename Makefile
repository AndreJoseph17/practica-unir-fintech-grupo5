# Variables
PYTHON = python3
SCRIPT = main.py
FILE = palabras.txt

# Instalación de dependencias (si existiera un requirements.txt en el futuro)
install:
	pip install -r requirements.txt

# Directiva para ejecutar en local sin Docker
run-local:
	@echo "Ejecutando aplicación en local..."
	$(PYTHON) $(SCRIPT)

# Ejecutar con fichero de palabras como parámetro
run-words:
	@echo "Ejecutando con fichero de palabras: $(FILE)"
	$(PYTHON) $(SCRIPT) $(FILE)
# Objetivo para ejecutar con parámetros (ejemplo: orden descendente)
run-desc:
	$(PYTHON) $(SCRIPT) --desc


# Limpieza de archivos temporales de Python
clean:
	rm -rf __pycache__
	rm -rf *.pyc